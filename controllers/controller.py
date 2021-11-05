from app import app

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/<hand1>/<hand2>')
def rps(hand1, hand2):
    return f"Hand1: {hand1}, Hand2: {hand2}"