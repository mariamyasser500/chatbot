from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello from Flask!"

if __name__ == '__main__':
    print(">>> Flask server starting...")
    app.run(debug=True)