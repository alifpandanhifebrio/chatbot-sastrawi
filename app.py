from flask import Flask, request, jsonify
from chat import get_response
from dotenv import load_dotenv
import os
from flask_cors import CORS

# Load environment variables
load_dotenv()

# Create Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Set Flask app debug mode based on environment variable FLASK_DEBUG
app.config['DEBUG'] = os.getenv('FLASK_DEBUG', False)

# Define predict route
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("message")

    if not text:
        return jsonify({"error": "No message provided"}), 400

    response = get_response(text)
    if not response:
        return jsonify({"error": "Jawaban tidak ditemukan"}), 500

    return jsonify({"answer": response})

# Run Flask app
if __name__ == "__main__":
    app.run()
