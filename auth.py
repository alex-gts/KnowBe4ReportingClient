# auth.py

def get_auth_header(api_key):
    """
    Generates the authentication header for API requests.

    Parameters:
    api_key (str): The API key for authenticating with the KnowBe4 API.

    Returns:
    dict: A dictionary with the Authorization header.
    """
    return {"Authorization": f"Bearer {api_key}"}
