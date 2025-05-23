# Rescue Pocket

A Python tool to interact with the Pocket API for retrieving and managing your saved articles.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- On macOS/Linux:
```bash
source venv/bin/activate
```
- On Windows:
```bash
.\venv\Scripts\activate
```

3. Install the package in development mode:
```bash
pip install -r requirements.txt
```

## Usage

1. Replace `YOUR_CONSUMER_KEY` in `main.py` with your Pocket consumer key.

2. Run the script:
```bash
python main.py
```

3. Follow the authentication flow in your browser when prompted.

## Features

- OAuth2 authentication with Pocket
- Retrieve your saved articles
- Display article titles and details

## Requirements

- Python 3.6 or higher
- requests library
