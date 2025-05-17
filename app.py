from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'my_super_secret_key_12345'

# Mock database (You can replace this with actual DB connection later)
users_db = {}

# Home route (Login Page)
@app.route('/')
def home():
    return render_template('index.html')

# Register route (Registration Page)
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        password = request.form['password']

        # Check if user already exists
        if phone in users_db:
            flash('Phone number already registered!', 'danger')
            return redirect(url_for('register'))

        # Hash the password
        hashed_password = generate_password_hash(password)

        # Store user data in 'users_db' (mock database)
        users_db[phone] = {'name': name, 'password': hashed_password}
        
        flash('Registration successful!', 'success')
        return redirect(url_for('home'))
    
    return render_template('register.html')

# Login route
@app.route('/login', methods=['POST'])
def login():
    phone = request.form['phone']
    password = request.form['password']
    
    if phone not in users_db:
        flash('Phone number not registered!', 'danger')
        return redirect(url_for('home'))
    
    # Check password
    if not check_password_hash(users_db[phone]['password'], password):
        flash('Incorrect password!', 'danger')
        return redirect(url_for('home'))
    
    # Save user info to session
    session['user'] = phone
    
    # Use POST-Redirect-GET to avoid resubmission
    return redirect(url_for('dashboard'))

# Dashboard route (Home after login)
@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        flash('Please log in first!', 'warning')
        return redirect(url_for('home'))
    
    user_phone = session['user']
    user_name = users_db[user_phone]['name']
    return render_template('dashboard.html', user_name=user_name)

# Crop Health route
@app.route('/crop_health')
def crop_health():
    if 'user' not in session:
        flash('Please log in first!', 'warning')
        return redirect(url_for('home'))
    return render_template('crop_health.html')

# Field Conditions route
@app.route('/field_conditions')
def field_conditions():
    if 'user' not in session:
        flash('Please log in first!', 'warning')
        return redirect(url_for('home'))
    return render_template('field_conditions.html')

# Irrigation route
@app.route('/irrigation')
def irrigation():
    if 'user' not in session:
        flash('Please log in first!', 'warning')
        return redirect(url_for('home'))
    return render_template('irrigation.html')

# Government Schemes route
@app.route('/schemes')
def schemes():
    if 'user' not in session:
        flash('Please log in first!', 'warning')
        return redirect(url_for('home'))
    return render_template('schemes.html')

# User Profile route
@app.route('/profile')
def profile():
    if 'user' not in session:
        flash('Please log in first!', 'warning')
        return redirect(url_for('home'))
    
    user_phone = session['user']
    user_name = users_db[user_phone]['name']
    return render_template('profile.html', user_name=user_name, user_phone=user_phone)

# Logout route
@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
