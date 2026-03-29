from flask import Flask, request, jsonify
from dotenv import load_dotenv
import requests
import os

app = Flask(__name__)

# These will eventually come from environment variables, not hardcoded
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
REDIRECT_URI = "https://fix.hackclub.com/callback"

@app.route('/')
def index():
    return 'FixHC backend is running!'

@app.route('/callback')
def callback():
    code = request.args.get('code')
                        
    if not code:
        return jsonify({"error": "No code provided"}), 400
    response = requests.post('https://auth.hackclub.com/oauth/token', json={
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "code": code,
        "grant_type": "authorization_code"
        })
    print(response.json())
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)