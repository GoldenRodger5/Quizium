from fastapi import FastAPI, UploadFile, File, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import os
import uuid
import random
from main import extract_text_from_pdf, generate_flashcards, check_answer, generate_hint, extract_text_from_url
from typing import Optional

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Templates and Static Files
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'json'}

# Create uploads directory if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# In-memory session storage (in production, use Redis or database)
sessions = {}

# Pydantic models
class StartSessionRequest(BaseModel):
    session_id: str
    num_questions: int = 10

class QuestionRequest(BaseModel):
    study_session_id: str

class AnswerRequest(BaseModel):
    study_session_id: str
    answer: str

class HintRequest(BaseModel):
    study_session_id: str

class URLRequest(BaseModel):
    url: str

class FlashcardsRequest(BaseModel):
    flashcards: list

def allowed_file(filename: str) -> bool:
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/health")
async def health_check():
    """Health check endpoint for Render"""
    return {"status": "healthy", "message": "Flashcard API is running"}

@app.get("/manifest.json")
async def get_manifest():
    """Serve PWA manifest file"""
    with open("static/manifest.json", "r") as f:
        manifest = json.load(f)
    return manifest

@app.get("/sw.js")
async def get_service_worker():
    """Serve service worker file"""
    with open("static/sw.js", "r") as f:
        sw_content = f.read()
    return HTMLResponse(content=sw_content, media_type="application/javascript")

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if not allowed_file(file.filename):
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a PDF or JSON file.")
    
    # Save file temporarily
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)
    
    file_extension = file.filename.rsplit('.', 1)[1].lower()
    
    try:
        if file_extension == 'pdf':
            # Process PDF and generate flashcards
            text = extract_text_from_pdf(file_path)
            if not text:
                raise HTTPException(status_code=400, detail="Failed to extract text from PDF")
            
            flashcards_data = generate_flashcards(text)
            if not flashcards_data:
                raise HTTPException(status_code=400, detail="Failed to generate flashcards")
            
            flashcards = flashcards_data.get('flashcards', [])
            
        elif file_extension == 'json':
            # Load existing flashcards JSON
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    flashcards = data.get('flashcards', [])
            except Exception as e:
                raise HTTPException(status_code=400, detail=f"Invalid JSON file: {str(e)}")
        
        # Store flashcards in session
        session_id = str(uuid.uuid4())
        sessions[session_id] = {
            'flashcards': flashcards,
            'study_session': None
        }
        
        return {
            'session_id': session_id,
            'flashcards': flashcards,
            'flashcard_count': len(flashcards),
            'message': f'Successfully loaded {len(flashcards)} flashcards'
        }
    
    finally:
        # Clean up uploaded file
        if os.path.exists(file_path):
            os.remove(file_path)

@app.post("/generate-from-url")
async def generate_flashcards_from_url(request: URLRequest):
    """API endpoint to generate flashcards from a URL."""
    try:
        print(f"Processing URL: {request.url}")
        text = extract_text_from_url(request.url)
        if not text:
            raise HTTPException(status_code=400, detail="Failed to extract content from URL")
        
        print(f"Extracted {len(text)} characters from URL")
        flashcards = generate_flashcards(text)
        if not flashcards:
            raise HTTPException(status_code=500, detail="Failed to generate flashcards")
        
        # Store flashcards in session for studying
        session_id = str(uuid.uuid4())
        sessions[session_id] = {
            'flashcards': flashcards.get('flashcards', []),
            'study_session': None
        }
        
        return {
            "session_id": session_id,
            "flashcards": flashcards.get('flashcards', []),
            "message": f"Generated {len(flashcards.get('flashcards', []))} flashcards from URL"
        }
    except Exception as e:
        print(f"Error processing URL: {e}")
        raise HTTPException(status_code=500, detail=f"Error processing URL: {str(e)}")

@app.post("/start_session")
async def start_session(request: StartSessionRequest):
    session_id = request.session_id
    num_questions = request.num_questions
    
    if not session_id:
        raise HTTPException(status_code=400, detail="No session_id provided")
    
    if session_id not in sessions:
        # This could happen if the server restarted and sessions were lost
        raise HTTPException(status_code=400, detail=f"Session expired or not found. Please regenerate your flashcards.")
    
    session_data = sessions[session_id]
    flashcards = session_data.get('flashcards', [])
    
    if not flashcards:
        raise HTTPException(status_code=400, detail="No flashcards found in session")
    
    # Shuffle and select requested number of flashcards
    flashcards_copy = flashcards.copy()  # Make a copy to avoid modifying original
    random.shuffle(flashcards_copy)
    selected_flashcards = flashcards_copy[:num_questions]
    
    # Store the selected flashcards for this session
    study_session_id = f"{session_id}_study"
    sessions[study_session_id] = {
        'flashcards': selected_flashcards,
        'current_question': 0,
        'score': 0,
        'total_questions': len(selected_flashcards)
    }
    
    return {
        'study_session_id': study_session_id,
        'total_questions': len(selected_flashcards)
    }

@app.post("/get_question")
async def get_question(request: QuestionRequest):
    study_session_id = request.study_session_id
    
    if not study_session_id or study_session_id not in sessions:
        raise HTTPException(status_code=400, detail="Invalid study session")
    
    study_data = sessions[study_session_id]
    current_q = study_data['current_question']
    
    if current_q >= len(study_data['flashcards']):
        # Session complete
        return {
            'complete': True,
            'final_score': study_data['score'],
            'total_questions': study_data['total_questions'],
            'percentage': (study_data['score'] / study_data['total_questions']) * 100
        }
    
    card = study_data['flashcards'][current_q]
    
    # Format question based on card type
    if card['type'] == 'question_answer':
        question = card['question']
        correct_answer = card['answer']
    elif card['type'] == 'vocabulary':
        question = f"What is the definition of: {card['term']}?"
        correct_answer = card['definition']
    elif card['type'] == 'fact':
        question = card['prompt']
        correct_answer = card['content']
    else:
        question = "Unknown question type"
        correct_answer = "Unknown answer"
    
    return {
        'question_number': current_q + 1,
        'total_questions': study_data['total_questions'],
        'question': question,
        'category': card.get('category', 'General'),
        'difficulty': card.get('difficulty', 'Unknown'),
        'current_score': study_data['score']
    }

@app.post("/submit_answer")
async def submit_answer(request: AnswerRequest):
    study_session_id = request.study_session_id
    user_answer = request.answer
    
    if not study_session_id or study_session_id not in sessions:
        raise HTTPException(status_code=400, detail="Invalid study session")
    
    study_data = sessions[study_session_id]
    current_q = study_data['current_question']
    card = study_data['flashcards'][current_q]
    
    # Get correct answer
    if card['type'] == 'question_answer':
        question = card['question']
        correct_answer = card['answer']
    elif card['type'] == 'vocabulary':
        question = f"What is the definition of: {card['term']}?"
        correct_answer = card['definition']
    elif card['type'] == 'fact':
        question = card['prompt']
        correct_answer = card['content']
    
    # Check answer
    is_correct = check_answer(question, correct_answer, user_answer)
    
    if is_correct:
        study_data['score'] += 1
    
    # Move to next question
    study_data['current_question'] += 1
    sessions[study_session_id] = study_data
    
    return {
        'correct': is_correct,
        'correct_answer': correct_answer,
        'new_score': study_data['score']
    }

@app.post("/get_hint")
async def get_hint(request: HintRequest):
    study_session_id = request.study_session_id
    
    if not study_session_id or study_session_id not in sessions:
        raise HTTPException(status_code=400, detail="Invalid study session")
    
    study_data = sessions[study_session_id]
    current_q = study_data['current_question']
    card = study_data['flashcards'][current_q]
    
    # Get question and answer
    if card['type'] == 'question_answer':
        question = card['question']
        correct_answer = card['answer']
    elif card['type'] == 'vocabulary':
        question = f"What is the definition of: {card['term']}?"
        correct_answer = card['definition']
    elif card['type'] == 'fact':
        question = card['prompt']
        correct_answer = card['content']
    
    hint = generate_hint(question, correct_answer)
    
    return {'hint': hint}

@app.post("/create_session_from_flashcards")
async def create_session_from_flashcards(request: FlashcardsRequest):
    """Create a new session from provided flashcards (used when session is lost)."""
    try:
        if not request.flashcards:
            raise HTTPException(status_code=400, detail="No flashcards provided")
        
        # Create a new session
        session_id = str(uuid.uuid4())
        sessions[session_id] = {
            'flashcards': request.flashcards,
            'study_session': None
        }
        
        return {
            'session_id': session_id,
            'flashcard_count': len(request.flashcards),
            'message': f'Successfully created session with {len(request.flashcards)} flashcards'
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating session: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app:app", host="0.0.0.0", port=port)
