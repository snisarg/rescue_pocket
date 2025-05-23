import requests
import webbrowser
from urllib.parse import urlencode

# Pocket API endpoints
REQUEST_TOKEN_URL = "https://getpocket.com/v3/oauth/request"
AUTHORIZE_URL = "https://getpocket.com/auth/authorize"
ACCESS_TOKEN_URL = "https://getpocket.com/v3/oauth/authorize"

# Your consumer key from Pocket
CONSUMER_KEY = "115064-2cc0de70bc2fd15d755c672"

def get_request_token():
    """Get a request token from Pocket"""
    data = {
        "consumer_key": CONSUMER_KEY,
        "redirect_uri": "pocketapp1234:authorizationFinished"
    }

    response = requests.post(REQUEST_TOKEN_URL, data=data, verify=False)
    if response.status_code == 200:
        return response.text.split('=')[1]
    else:
        raise Exception(f"Failed to get request token: {response.text}")

def authorize_app(request_token):
    """Open browser for user authorization"""
    auth_url = f"{AUTHORIZE_URL}?{urlencode({'request_token': request_token, 'redirect_uri': 'pocketapp1234:authorizationFinished'})}"
    webbrowser.open(auth_url)
    input("After you've authorized the app in your browser, the window will not close automatically. Just come back here and press Enter...")

def get_access_token(request_token):
    """Exchange request token for access token"""
    data = {
        "consumer_key": CONSUMER_KEY,
        "code": request_token
    }

    response = requests.post(ACCESS_TOKEN_URL, data=data, verify=False)
    if response.status_code == 200:
        return response.text.split('&')[0].split('=')[1]
    else:
        raise Exception(f"Failed to get access token: {response.text}")

def authenticate():
    """Complete authentication flow and return access token"""
    # Step 1: Get request token
    request_token = get_request_token()
    print(f"Request token: {request_token}")

    # Step 2: Authorize the app
    authorize_app(request_token)

    # Step 3: Get access token
    access_token = get_access_token(request_token)
    print(f"Access token: {access_token}")

    return access_token
