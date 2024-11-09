from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a randomly generated secret key for session security

# Static user data with hashed passwords
users = {
    "user1": generate_password_hash("password123"),  # Username: user1, Password: password123
    "user2": generate_password_hash("securepassword"),  # Username: user2, Password: securepassword
}

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Validate username and password
        if username in users and check_password_hash(users[username], password):
            session['user_id'] = username
            flash("Login berhasil!", "success")
            return redirect(url_for('dashboard'))
        else:
            flash("Username atau password salah.", "danger")
    
    return render_template('login2.html')  # Ensure this template exists in the 'templates' folder

# Route for logout
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash("Anda telah keluar.", "info")
    return redirect(url_for('login'))

# Route for the dashboard page after login
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash("Silakan login terlebih dahulu.", "warning")
        return redirect(url_for('login'))
    return render_template('dashboard2.html', username=session['user_id'])  # Ensure this template exists in the 'templates' folder

if __name__ == '__main__':
    app.run(debug=True)
