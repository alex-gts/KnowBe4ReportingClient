import requests

class APIError(Exception):
    """Custom exception class for API errors."""
    def __init__(self, status_code, message=None):
        super().__init__(message or f"API Error with status code {status_code}")
        self.status_code = status_code
        self.message = message

def handle_response(response):
    """Handles API responses, raising exceptions for error codes."""
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 400:
        raise APIError(400, "Bad Request - The request was invalid or cannot be served.")
    elif response.status_code == 401:
        raise APIError(401, "Unauthorized - The request requires user authentication.")
    elif response.status_code == 403:
        raise APIError(403, "Forbidden - The server understood the request, but is refusing to fulfill it.")
    elif response.status_code == 404:
        raise APIError(404, "Not Found - The server has not found anything matching the request URI.")
    elif response.status_code == 500:
        raise APIError(500, "Internal Server Error - The server encountered an unexpected condition.")
    else:
        # Generic error for other status codes
        raise APIError(response.status_code, f"Unexpected API error: {response.text}")

# You can add other utility functions here as needed
