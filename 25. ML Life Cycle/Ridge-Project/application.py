from flask import Flask

application = Flask(__name__)
app = application  # For compatibility with some hosting services

@app.route('/')
def home():
    return "Hello, Flask is working!"

if __name__ == '__main__':
    app.run(debug=True)