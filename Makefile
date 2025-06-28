# Flashcard App - Quick Commands
# Usage: make [command]

.PHONY: local deploy test-render install clean status help

# Default target
help:
	@echo "🚀 Flashcard App - Quick Commands"
	@echo ""
	@echo "📋 Available commands:"
	@echo "  make local        Start local development server"
	@echo "  make test-render  Test Render deployment locally"
	@echo "  make deploy       Check deployment readiness"
	@echo "  make install      Install dependencies"
	@echo "  make clean        Clean up cache files"
	@echo "  make status       Show project status"
	@echo ""

# Start local development server
local:
	@echo "🚀 Starting local development server..."
	uvicorn app:app --host 0.0.0.0 --port 8000 --reload

# Test Render deployment configuration
test-render:
	@echo "🧪 Testing Render configuration..."
	PORT=10000 uvicorn app:app --host 0.0.0.0 --port $$PORT

# Check deployment readiness
deploy:
	@echo "🚀 Checking deployment readiness..."
	@./dev.sh deploy

# Install dependencies
install:
	@echo "📦 Installing dependencies..."
	pip install -r requirements.txt

# Clean up
clean:
	@echo "🧹 Cleaning up..."
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
	@echo "✅ Cleanup complete!"

# Show status
status:
	@./dev.sh status
