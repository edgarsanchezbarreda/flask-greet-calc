from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def home_page():
    html = """
    <html>
        <body>
            <h1>Home Page</h1>
            <p>Welcome to my simple App!</p>
        </body>
    </html>
    """
    return html

@app.route('/welcome')
def welcome():
    return "welcome"

@app.route('/welcome/home')
def home():
    return "welcome home"

@app.route('/welcome/back')
def back():
    return "welcome back"