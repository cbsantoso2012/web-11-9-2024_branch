from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Kunci rahasia untuk flash message


# Route untuk halaman login
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Contoh validasi sederhana
        if username == 'admin' and password == 'password':
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'danger')

    return render_template('login.html')


# Route untuk halaman dashboard setelah login sukses
@app.route('/dashboard')
def dashboard():
    return "Welcome to the dashboard!"


if __name__ == '__main__':
    app.run(debug=True)
