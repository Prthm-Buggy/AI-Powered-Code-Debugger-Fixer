from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
CORS(app)
app.secret_key = "your_secret_key"  # Change this to a strong secret key

# Dummy user database (Replace with a real database)
users = {
    "admin": generate_password_hash("password123"),
    "user": generate_password_hash("test123")
}

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

        # Check credentials securely
        if username in users and check_password_hash(users[username], password):
            session['user'] = username
            flash("Login successful!", "success")
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid username or password.", "danger")

    return render_template('login.html')

# Dashboard (Only accessible after login)
@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        flash("Please log in first.", "warning")
        return redirect(url_for('login'))
    return render_template('dashboard.html', username=session['user'])

# Logout
@app.route('/logout')
def logout():
    session.pop('user', None)
    flash("You have been logged out.", "info")
    return redirect(url_for('login'))

# Error Handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
