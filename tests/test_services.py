import pytest
from app.services.ai_service import generate_response

def test_generate_response(monkeypatch):
    class MockResponse:
        def __init__(self, content):
            self.choices = [{'message': {'content': content}}]

    def mock_create(*args, **kwargs):
        return MockResponse("This is a test response.")

    monkeypatch.setattr("openai.ChatCompletion.create", mock_create)
    response = generate_response("Test input")
    assert response == "This is a test response."