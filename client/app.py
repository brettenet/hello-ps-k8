from flask import Flask, jsonify
import requests
import os 
from dotenv import load_dotenv
from urllib.parse import urljoin

# Load .env file
load_dotenv()

app = Flask(__name__)

server_url = os.getenv("SERVER_URL")
if not server_url:
    raise ValueError("SERVER_URL environment variable is not set")

end_point = urljoin(server_url, "/api/get-string")

@app.route('/', methods=['GET'])
@app.route('/api/message', methods=['GET'])
def get_message():
    try:
        response = requests.get(end_point)
        response.raise_for_status()
        data = response.json()
        return jsonify({"message": data["message"]})
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
