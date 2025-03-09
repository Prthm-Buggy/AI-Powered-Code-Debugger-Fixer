from flask import Flask, render_template, request, redirect, url_for, session
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.secret_key = "your_secret_key"  # Change this to a strong secret key

# Dummy user database (Replace with a real database)
users = {"admin": "password123", "user": "test123"}

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Features Page
@app.route('/features')
def features():
    return render_template('features.html')

# About Page
@app.route('/about')
def about():
    return render_template('about.html')

# Try Page
@app.route('/try')
def try_now():
    return render_template('try.html')

# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check credentials
        if username in users and users[username] == password:
            session['user'] = username
            return redirect(url_for('dashboard'))
        else:
            return "Invalid username or password. <a href='/login'>Try again</a>"

    return render_template('login.html')

# Dashboard (Only accessible after login)
@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', username=session['user'])

# Logout
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
