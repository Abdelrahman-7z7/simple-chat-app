import requests
from bs4 import BeautifulSoup

def test_homepage_content():
    try:
        # Send request to the homepage
        response = requests.get("http://localhost:8080")
        assert response.status_code == 200, f"Homepage not accessible. Status code: {response.status_code}"

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Check if the page contains a specific title or content
        title = soup.find('title').text
        assert title == "WebSocket Chat", f"Title mismatch: Expected 'WebSocket Chat', got '{title}'"
        
        # Check if the homepage contains specific text (e.g., a placeholder in the input box)
        input_placeholder = soup.find('input', {'id': 'messageInput'})['placeholder']
        assert input_placeholder == "Type a message...", f"Placeholder mismatch: Expected 'Type a message...', got '{input_placeholder}'"
        
        print("Homepage content is correct.")
        
    except Exception as e:
        print(f"Error testing homepage content: {e}")

if __name__ == "__main__":
    test_homepage_content()
