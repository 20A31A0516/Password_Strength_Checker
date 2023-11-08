from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_password_strength(password):
    # Define conditions for a strong password
    conditions = [
        lambda s: any(c.isupper() for c in s),
        lambda s: any(c.islower() for c in s),
        lambda s: any(c.isdigit() for c in s),
        lambda s: len(s) >= 8
    ]

    # Check password against conditions
    strength = all(condition(password) for condition in conditions)
    return strength

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    password = request.form['password']
    is_password_strong = check_password_strength(password)
    return render_template('result.html', is_password_strong=is_password_strong)

if __name__ == '__main__':
    app.run(debug=True)
