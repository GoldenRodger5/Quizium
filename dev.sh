#!/bin/bash

# Development and Deployment Script for Flashcard App
# Usage: ./dev.sh [command]

case "$1" in
    "local" | "dev")
        echo "🚀 Starting local development server..."
        echo "📍 Server will be available at: http://localhost:8000"
        echo "📱 Web app will be available at: http://localhost:8000"
        echo ""
        uvicorn app:app --host 0.0.0.0 --port 8000 --reload
        ;;
    
    "local-main")
        echo "🚀 Starting local server using main.py..."
        echo "📍 Server will be available at: http://localhost:8000"
        echo "📱 Web app will be available at: http://localhost:8000/app"
        echo ""
        uvicorn main:app --host 0.0.0.0 --port 8000 --reload
        ;;
    
    "render-test")
        echo "🧪 Testing Render deployment configuration locally..."
        echo "📍 Testing with PORT environment variable"
        echo "📱 Web app will be available at: http://localhost:10000"
        echo ""
        PORT=10000 uvicorn app:app --host 0.0.0.0 --port $PORT
        ;;
    
    "deploy")
        echo "🚀 Preparing for Render deployment..."
        echo "📦 Checking requirements.txt..."
        if [ -f "requirements.txt" ]; then
            echo "✅ requirements.txt found"
        else
            echo "❌ requirements.txt not found!"
            exit 1
        fi
        
        echo "📦 Checking render.yaml..."
        if [ -f "render.yaml" ]; then
            echo "✅ render.yaml found"
        else
            echo "❌ render.yaml not found!"
            exit 1
        fi
        
        echo "🔍 Checking if CLAUDE_API_KEY is mentioned in render.yaml..."
        if grep -q "CLAUDE_API_KEY" render.yaml; then
            echo "✅ CLAUDE_API_KEY configured in render.yaml"
        else
            echo "⚠️  Remember to set CLAUDE_API_KEY in Render dashboard"
        fi
        
        echo ""
        echo "🎯 Ready for Render deployment!"
        echo "📋 Next steps:"
        echo "   1. Push to GitHub: git add . && git commit -m 'Deploy to Render' && git push"
        echo "   2. Connect repository to Render"
        echo "   3. Set CLAUDE_API_KEY environment variable in Render dashboard"
        echo "   4. Deploy!"
        ;;
    
    "install")
        echo "📦 Installing dependencies..."
        pip install -r requirements.txt
        echo "✅ Dependencies installed!"
        ;;
    
    "test-cli")
        echo "🧪 Testing CLI functionality..."
        echo "Available commands:"
        echo "  python main.py 'https://en.wikipedia.org/wiki/Artificial_Intelligence'"
        echo "  python main.py document.pdf"
        echo "  python main.py study flashcards.json"
        ;;
    
    "clean")
        echo "🧹 Cleaning up..."
        find . -name "*.pyc" -delete
        find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
        echo "✅ Cleanup complete!"
        ;;
    
    "status")
        echo "📊 Project Status:"
        echo "📁 Current directory: $(pwd)"
        echo "🐍 Python version: $(python --version 2>&1)"
        echo "📦 FastAPI installed: $(pip show fastapi 2>/dev/null | grep Version || echo 'Not installed')"
        echo "🤖 Anthropic installed: $(pip show anthropic 2>/dev/null | grep Version || echo 'Not installed')"
        echo ""
        echo "📂 Project files:"
        ls -la *.py *.yaml *.txt 2>/dev/null || echo "Some files missing"
        ;;
    
    *)
        echo "🚀 Flashcard App Development Script"
        echo ""
        echo "Usage: ./dev.sh [command]"
        echo ""
        echo "📋 Available commands:"
        echo "  local         Start local development server (app.py) with auto-reload"
        echo "  local-main    Start local server using main.py"
        echo "  render-test   Test Render deployment configuration locally"
        echo "  deploy        Check deployment readiness and show next steps"
        echo "  install       Install all dependencies from requirements.txt"
        echo "  test-cli      Show CLI usage examples"
        echo "  clean         Clean up Python cache files"
        echo "  status        Show project status and versions"
        echo ""
        echo "💡 Quick start:"
        echo "  ./dev.sh install   # Install dependencies"
        echo "  ./dev.sh local     # Start development server"
        echo ""
        ;;
esac
