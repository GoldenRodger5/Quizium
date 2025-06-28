# PDF to Flashcards Generator

A simple Python script that extracts text from PDF files and uses Claude AI to generate comprehensive flashcards for studying.

## Features

- Extract text from PDF files
- Generate multiple types of flashcards:
  - Question-Answer pairs
  - Vocabulary terms with definitions
  - Important facts and figures
- Output flashcards as JSON format
- Save results to file and display in console

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
