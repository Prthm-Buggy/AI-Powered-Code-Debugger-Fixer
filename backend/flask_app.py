from flask import Flask, request, jsonify
import openai
import subprocess
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows frontend requests

# Set up OpenAI API key (if using GPT)
openai.api_key = ""

def lint_python_code(code):
    """Uses pylint to analyze Python code and return suggestions"""
    with open("temp.py", "w") as f:
        f.write(code)

    result = subprocess.run(["pylint", "temp.py"], capture_output=True, text=True)
    return result.stdout

@app.route('/fix_code', methods=['POST'])
def fix_code():
    data = request.json
    user_code = data.get("code", "")

    if not user_code:
        return jsonify({"error": "No code provided"}), 400

    # AI-based Fixing (Using OpenAI GPT)
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a code debugger."},
                  {"role": "user", "content": f"Fix the following code and explain the fixes:\n{user_code}"}]
    )
    
    ai_fixed_code = response["choices"][0]["message"]["content"]

    # Linter-based Fixing (For Python Code)
    linter_feedback = lint_python_code(user_code)

    return jsonify({
        "original_code": user_code,
        "fixed_code": ai_fixed_code,
        "linter_feedback": linter_feedback
    })

if __name__ == '__main__':
    app.run(debug=True)
