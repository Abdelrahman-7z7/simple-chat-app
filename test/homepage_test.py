import requests

def test_homepage():
    try:
        response = requests.get("http://localhost:8080")
        assert response.status_code == 200, f"Homepage not accessible. Status code: {response.status_code}"
        print("Homepage is accessible.")
    except Exception as e:
        print(f"Error testing homepage: {e}")

if __name__ == "__main__":
    test_homepage()
