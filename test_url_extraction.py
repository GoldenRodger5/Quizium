#!/usr/bin/env python3
"""
Test script for web content extraction functionality
"""
import sys
import os
sys.path.append('/Users/isaacmineo/Main/projects/flash-cards')

from main import extract_text_from_url, extract_general_webpage

def test_url_extraction():
    """Test URL content extraction without needing API key"""
    test_url = "https://en.wikipedia.org/wiki/Artificial_intelligence"
    
    print(f"Testing URL extraction for: {test_url}")
    print("-" * 50)
    
    try:
        # Test the URL extraction
        text = extract_text_from_url(test_url)
        
        if text:
            print(f"✅ Successfully extracted content!")
            print(f"Content length: {len(text)} characters")
            print(f"First 200 characters: {text[:200]}...")
            return True
        else:
            print("❌ Failed to extract content")
            return False
            
    except Exception as e:
        print(f"❌ Error during extraction: {e}")
        return False

if __name__ == "__main__":
    success = test_url_extraction()
    sys.exit(0 if success else 1)
