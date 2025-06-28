# 🧠 AI Flashcard Generator & Study Assistant

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg)

**An intelligent web application that transforms PDFs and web content into interactive flashcards using Claude AI, featuring a beautiful study interface with advanced learning analytics.**

[🚀 Live Demo](https://your-app.onrender.com) | [📖 Documentation](#documentation) | [🐛 Report Bug](https://github.com/your-username/flashcard-app/issues) | [💡 Request Feature](https://github.com/your-username/flashcard-app/issues)

</div>

---

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Installation & Setup](#installation--setup)
- [Usage Guide](#usage-guide)
- [API Documentation](#api-documentation)
- [Deployment](#deployment)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

The **AI Flashcard Generator & Study Assistant** is a modern, full-stack web application that revolutionizes the way students and professionals create and study flashcards. By leveraging cutting-edge AI technology and intuitive design, it transforms static study materials into dynamic, interactive learning experiences.

### 🌟 What Makes It Special

- **AI-Powered Content Extraction**: Automatically generates high-quality flashcards from PDFs, Wikipedia articles, and web content
- **Intelligent Study Assistant**: Uses Claude AI for smart answer evaluation, hint generation, and adaptive learning
- **Beautiful Interactive Interface**: 3D flip animations, responsive design, and smooth user experience
- **Persistent Study Sessions**: Resume study sessions across browser tabs without losing progress
- **Multi-Format Support**: Works with PDFs, URLs, and existing JSON flashcard files

---

## ✨ Key Features

### 📚 Content Processing
- **📄 PDF Processing**: Extract text from PDF documents and auto-generate flashcards
- **🌐 Web Content Integration**: Support for Wikipedia articles and general web pages
- **📝 Manual Upload**: Import existing flashcard sets in JSON format
- **🔄 Batch Processing**: Handle multiple content sources in a single session

### 🎴 Interactive Flashcards
- **3D Flip Animations**: Beautiful card transitions with smooth animations
- **Multiple Card Types**: Question-Answer, Vocabulary, and Fact-based cards
- **Category Organization**: Automatic categorization by topic and difficulty
- **Navigation Controls**: Easy browsing with previous/next buttons and counters

### 🎯 Smart Study System
- **AI Answer Evaluation**: Flexible answer checking using Claude AI
- **Intelligent Hints**: Context-aware hints that guide without revealing answers
- **Progress Tracking**: Real-time score tracking and completion percentage
- **Adaptive Learning**: Skip difficult questions and return to them later

### 🔄 Session Management
- **Persistent Sessions**: Study progress maintained across browser tabs
- **Auto-Recovery**: Automatic session restoration after server restarts
- **Multiple Study Modes**: Browse mode for review, study mode for testing
- **Customizable Sessions**: Choose number of questions and difficulty levels

### 📱 Modern UI/UX
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile
- **Dark/Light Themes**: Comfortable viewing in any environment
- **Progress Visualization**: Interactive progress bars and score displays
- **Accessibility**: WCAG compliant with keyboard navigation support

---

## 🛠 Tech Stack

### Backend
- **[FastAPI](https://fastapi.tiangolo.com/)** - Modern, fast web framework for building APIs
- **[Python 3.11+](https://www.python.org/)** - Core programming language
- **[Anthropic Claude AI](https://www.anthropic.com/)** - AI-powered content generation and evaluation
- **[Uvicorn](https://www.uvicorn.org/)** - ASGI server for production deployment

### Frontend
- **HTML5** - Semantic markup with modern standards
- **CSS3** - Advanced styling with animations and responsive design
- **Vanilla JavaScript** - No frameworks, pure ES6+ for optimal performance
- **Web APIs** - File handling, fetch API, and local storage

### Data Processing
- **[PyPDF2](https://pypdf2.readthedocs.io/)** - PDF text extraction
- **[BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)** - Web scraping and HTML parsing
- **[Requests](https://docs.python-requests.org/)** - HTTP client for web content fetching

### Development & Deployment
- **[Jinja2](https://jinja.palletsprojects.com/)** - Template engine for dynamic HTML
- **[python-multipart](https://github.com/andrew-d/python-multipart)** - File upload handling
- **[python-dotenv](https://github.com/theskumar/python-dotenv)** - Environment variable management
- **[Render](https://render.com/)** - Cloud deployment platform

---

## 🏗 Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Backend       │    │  External APIs  │
│   (HTML/CSS/JS) │◄───┤   (FastAPI)     │◄───┤  (Claude AI)    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         │                       │                       │
    ┌────▼────┐              ┌───▼───┐              ┌────▼────┐
    │ UI/UX   │              │Session│              │Content  │
    │Components│              │Manager│              │Processors│
    └─────────┘              └───────┘              └─────────┘
```

### Core Components

1. **Content Processors**: Handle PDF extraction and web scraping
2. **AI Integration**: Claude AI for flashcard generation, answer evaluation, and hints
3. **Session Manager**: In-memory session storage with auto-recovery capabilities
4. **API Layer**: RESTful endpoints for all frontend interactions
5. **Frontend Controller**: Manages UI state, tab switching, and user interactions

---

## 🚀 Installation & Setup

### Prerequisites

- **Python 3.11 or higher**
- **Git** for version control
- **Claude AI API Key** ([Get one here](https://console.anthropic.com/))

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/flashcard-app.git
cd flashcard-app
```

### 2. Create Virtual Environment

```bash
# Using venv (recommended)
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Configuration

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env file and add your Claude API key
# CLAUDE_API_KEY=your_actual_api_key_here
```

### 5. Verify Installation

```bash
# Test the installation
python -c "import fastapi, anthropic, PyPDF2; print('✅ All dependencies installed successfully!')"
```

---

## � Usage Guide

### 🚀 Starting the Application

#### Option 1: Using the Development Script (Recommended)
```bash
# Start local development server
./dev.sh local
```

#### Option 2: Direct Python Execution
```bash
# Start with uvicorn
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

#### Option 3: Using Make Commands
```bash
# If you have make installed
make local
```

The application will be available at: **http://localhost:8000**

### 🎯 Creating Flashcards

#### From PDF Files
1. Click **"Choose File"** in the upload section
2. Select a PDF file from your computer
3. Wait for processing (typically 10-30 seconds)
4. Review generated flashcards in the tabbed interface

#### From Web Content
1. Enter a URL in the **"Generate from Web Content"** section
2. Supported sources:
   - **Wikipedia**: `https://en.wikipedia.org/wiki/Topic`
   - **Articles**: Any web page with readable content
3. Click **"🚀 Generate Flashcards"**
4. Processing time varies based on content length

#### From Existing JSON
1. Upload a pre-existing flashcard JSON file
2. Format should match the application's schema:
```json
{
  "flashcards": [
    {
      "type": "question_answer",
      "category": "science",
      "difficulty": "medium",
      "question": "What is photosynthesis?",
      "answer": "The process by which plants convert sunlight into energy"
    }
  ]
}
```

### 📚 Studying with Flashcards

#### Browse Mode
- **Navigate**: Use Previous/Next buttons or click cards
- **Flip Cards**: Click on any card or use the "🔄 Flip Card" button
- **Visual Learning**: 3D animations provide engaging study experience

#### Study Mode
1. Click **"🎯 Study Mode"** tab
2. Set number of questions (1 to total available)
3. Click **"🎯 Start Study Session"**

#### Study Session Features
- **Answer Input**: Type answers in the text area
- **AI Evaluation**: Flexible answer checking that accepts variations
- **Hints**: Click "💡 Get Hint" for guidance
- **Skip Option**: Use "⏭️ Skip" for difficult questions
- **Progress Tracking**: Real-time score and progress visualization

#### Session Management
- **Tab Switching**: Move between Browse and Study modes freely
- **Progress Persistence**: Study sessions resume where you left off
- **Restart Capability**: Use "🔄 Restart Study Session" anytime

### 🔄 Advanced Features

#### Multiple Content Sources
- Generate flashcards from multiple sources in one session
- Each new source replaces the current flashcard set
- Previous study progress is automatically reset

#### Session Recovery
- If the server restarts, sessions are automatically recovered
- Flashcards stored in browser ensure continuity
- Graceful error handling with user-friendly messages

---

## 📡 API Documentation

### Core Endpoints

#### Generate Flashcards from URL
```http
POST /generate-from-url
Content-Type: application/json

{
  "url": "https://en.wikipedia.org/wiki/Machine_Learning"
}
```

#### Upload File
```http
POST /upload
Content-Type: multipart/form-data

file: <PDF or JSON file>
```

#### Start Study Session
```http
POST /start_session
Content-Type: application/json

{
  "session_id": "uuid-string",
  "num_questions": 10
}
```

#### Submit Answer
```http
POST /submit_answer
Content-Type: application/json

{
  "study_session_id": "uuid-string",
  "answer": "user answer text"
}
```

#### Get Hint
```http
POST /get_hint
Content-Type: application/json

{
  "study_session_id": "uuid-string"
}
```

### Response Formats

#### Flashcard Object
```json
{
  "type": "question_answer" | "vocabulary" | "fact",
  "category": "string",
  "difficulty": "easy" | "medium" | "hard",
  "question": "string",
  "answer": "string"
}
```

#### Study Session Response
```json
{
  "study_session_id": "string",
  "total_questions": "number"
}
```

---

## 🌐 Deployment

### Render Deployment (Recommended)

#### 1. Prepare for Deployment
```bash
# Check deployment readiness
./dev.sh deploy
```

#### 2. Push to GitHub
```bash
git add .
git commit -m "Deploy to production"
git push origin main
```

#### 3. Deploy on Render
1. Go to [render.com](https://render.com) and sign up/login
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository
4. Render will detect the `render.yaml` configuration automatically
5. Set environment variables:
   - `CLAUDE_API_KEY`: Your Anthropic API key
6. Click **"Create Web Service"**

#### 4. Configuration Details
The `render.yaml` file includes:
```yaml
services:
  - type: web
    name: flashcard-app
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn app:app --host 0.0.0.0 --port $PORT
    envVars:
      - key: CLAUDE_API_KEY
        sync: false
```

### Alternative Deployment Options

#### Heroku
```bash
# Install Heroku CLI and login
heroku create your-app-name
heroku config:set CLAUDE_API_KEY=your_api_key
git push heroku main
```

#### Docker
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## 🛠 Development

### Project Structure
```
flashcard-app/
├── app.py                 # Main FastAPI application
├── main.py               # CLI interface and core functions
├── templates/
│   └── index.html       # Frontend application
├── uploads/             # Temporary file storage
├── requirements.txt     # Python dependencies
├── render.yaml         # Render deployment config
├── runtime.txt         # Python version specification
├── dev.sh             # Development scripts
├── Makefile           # Make commands
└── README.md          # This file
```

### Development Commands

```bash
# Start development server with auto-reload
./dev.sh local

# Test Render deployment locally
./dev.sh render-test

# Run CLI version
python main.py document.pdf
python main.py https://en.wikipedia.org/wiki/Topic
python main.py study flashcards.json

# Clean up cache and temporary files
./dev.sh clean

# Check project status
./dev.sh status
```

### Code Style and Standards

- **PEP 8**: Python code formatting
- **Type Hints**: Used throughout for better code documentation
- **Error Handling**: Comprehensive exception handling with user-friendly messages
- **Documentation**: Inline comments and docstrings for all functions
- **Security**: Input validation and sanitization for all user inputs

### Testing

```bash
# Test PDF processing
python -c "from main import extract_text_from_pdf; print('PDF extraction:', bool(extract_text_from_pdf('test.pdf')))"

# Test web scraping
python -c "from main import extract_text_from_url; print('URL extraction:', bool(extract_text_from_url('https://en.wikipedia.org/wiki/Python')))"

# Test API endpoints
curl -X GET http://localhost:8000/health
```

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

### 1. Fork and Clone
```bash
git fork https://github.com/your-username/flashcard-app.git
git clone https://github.com/your-username/flashcard-app.git
cd flashcard-app
```

### 2. Create Feature Branch
```bash
git checkout -b feature/amazing-feature
```

### 3. Development Setup
```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 4. Make Changes
- Follow existing code style
- Add tests for new features
- Update documentation as needed

### 5. Commit and Push
```bash
git add .
git commit -m "Add amazing feature"
git push origin feature/amazing-feature
```

### 6. Create Pull Request
- Describe your changes clearly
- Include screenshots for UI changes
- Reference any related issues

### Areas for Contribution
- **New Content Sources**: Add support for more websites and formats
- **UI Improvements**: Enhance design and user experience
- **Performance**: Optimize loading times and memory usage
- **Testing**: Add comprehensive test coverage
- **Documentation**: Improve guides and API docs

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 Flashcard App Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 🙏 Acknowledgments

- **[Anthropic](https://www.anthropic.com/)** for Claude AI API
- **[FastAPI](https://fastapi.tiangolo.com/)** for the excellent web framework
- **[Render](https://render.com/)** for seamless deployment platform
- **Open Source Community** for the amazing libraries and tools

---

## 📞 Support

- **📧 Email**: support@flashcard-app.com
- **🐛 Issues**: [GitHub Issues](https://github.com/your-username/flashcard-app/issues)
- **💬 Discussions**: [GitHub Discussions](https://github.com/your-username/flashcard-app/discussions)
- **📚 Documentation**: [Wiki](https://github.com/your-username/flashcard-app/wiki)

---

<div align="center">

**⭐ Star this repository if it helped you learn better! ⭐**

Made with ❤️ by developers who believe in the power of AI-enhanced learning.

</div>

# Test Render configuration
npm run test-render
```

### Option 4: Direct Commands
```bash
# Development server
uvicorn app:app --host 0.0.0.0 --port 8000 --reload

# Render test
PORT=10000 uvicorn app:app --host 0.0.0.0 --port $PORT
```

## 🛠️ Development vs Production

### 🖥️ Local Development
- **File**: Uses `app.py`
- **Command**: `./dev.sh local` or `make local`
- **URL**: `http://localhost:8000`
- **Features**: Auto-reload, debug mode, local file uploads

### 🌐 Render Deployment  
- **File**: Uses `app.py` (same file!)
- **Command**: Automatically uses `render.yaml` configuration
- **URL**: `https://your-app.onrender.com`
- **Features**: Production optimizations, environment variables

## 📋 Available Commands

| Command | Description |
|---------|-------------|
| `./dev.sh local` | Start local development server |
| `./dev.sh render-test` | Test Render deployment locally |
| `./dev.sh deploy` | Check deployment readiness |
| `./dev.sh install` | Install dependencies |
| `./dev.sh test-cli` | Show CLI usage examples |
| `./dev.sh clean` | Clean up cache files |
| `./dev.sh status` | Show project status |

## Installation

1. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the script with a PDF file as an argument:

```bash
python main.py your_document.pdf
```

### Example:
```bash
python main.py textbook_chapter.pdf
```

This will:
1. Extract text from `textbook_chapter.pdf`
2. Send the text to Claude AI to generate flashcards
3. Save the flashcards to `textbook_chapter_flashcards.json`
4. Display the flashcards in the console

## Output Format

The generated flashcards are saved as JSON with the following structure:

```json
{
  "flashcards": [
    {
      "type": "question_answer",
      "question": "What is photosynthesis?",
      "answer": "The process by which plants convert sunlight into energy..."
    },
    {
      "type": "vocabulary",
      "term": "Chlorophyll",
      "definition": "The green pigment in plants that captures light energy..."
    },
    {
      "type": "fact",
      "prompt": "Chemical formula for photosynthesis",
      "content": "6CO2 + 6H2O + light energy → C6H12O6 + 6O2"
    }
  ]
}
```

## Requirements

- Python 3.7+
- PyPDF2 (for PDF text extraction)
- anthropic (for Claude AI integration)
- Valid Claude API key (already configured in the script)

## Notes

- The script works best with text-based PDFs (not scanned images)
- Large PDFs may take longer to process
- The quality of flashcards depends on the quality and structure of the source text
