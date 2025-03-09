from flask import Flask, request, render_template
from flask_cors import CORS
from debugger import analyze_code

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/try')
def try_now():
    return render_template('try.html')

if __name__ == '__main__':
    app.run(debug=True)
