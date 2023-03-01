from flask import Flask, session, redirect, url_for, render_template
import json
import psycopg2
from requests import Request, Session, request
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# Define a route for the sign up page
# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         # Get the form data
#         full_name = request.form['full_name']
#         email = request.form['email']
#         password = request.form['password']
#         repeat_password = request.form['repeat_password']

#         # Check if the email address is already in use
#         cur = conn.cursor()
#         cur.execute("SELECT * FROM users WHERE email=%s", (email,))
#         if cur.fetchone() is not None:
#             return "Email address already in use"
#         # Check if the passwords match
#         if password != repeat_password:
#             return "Passwords do not match"
#         # Hash the password (you should use a stronger hashing algorithm in production)
#         password_hash = hash(password)
#         # Insert the new user into the database
#         cur.execute("INSERT INTO users (full_name, email, password_hash) VALUES (%s, %s, %s)", (full_name, email, password_hash))
#         conn.commit()
#         # Redirect to the dashboard
#         return redirect('/dashboard')
#     # If the request method is GET, just render the sign up page
#     return render_template('signup.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']
        
#         cur = conn.cursor()
#         cur.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
#         user = cur.fetchone()
        
#         if user is None:
#             error = 'Invalid email or password. Please try again.'
#             return render_template('login.html', error=error)
#         else:
#             session['user_id'] = user[0]  # save user id to session
#             return redirect(url_for('dashboard'))
#     else:
#         return render_template('login.html')

@app.route('/signup')
def signup():
    # your logic here
    return render_template('signup.html')
# @app.route('/dashboard', methods=['GET', 'POST'])
# def dashboard():
# 	if request.method == 'POST': 
# 		name = request.form.get('name')
# 		email = request.form.get('email')
# 		password = request.form.get('password')
# 		confirm_password = request.form.get('confirm_password')

# 		if password != confirm_password:
# 			flash('Passwords do not match!')
# 			return redirect(url_for('dashboard'))

# 		# Process the form data here
# 		# Create user in database
# 		# Redirect user to dashboard 
# 		return redirect(url_for('dashboard'))

# 	return render_template('dashboard.html')
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
@app.route('/contact/')
def contact():
    return render_template('contact.html')
@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)
