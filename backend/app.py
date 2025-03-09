#flask run --reload
from flask import Flask, request, jsonify
from flask_cors import CORS
from debugger import analyze_code

app = Flask(__name__)
CORS(app)  # Allow frontend to access API

@app.route('/')
def home():
    return "Welcome to the AI Codesdf Debugger API!"

@app.route('/debug', methods=['POST'])
def debug_code():
    data = request.json
    code = data.get('code', '')

    if not code:
        return jsonify({'error': 'No code provided'}), 400

    result = analyze_code(code)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
