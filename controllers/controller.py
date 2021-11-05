from app import app
from models.run_game import run_game

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/<hand1>/<hand2>')
def rps(hand1, hand2):
    winner = run_game(hand1, hand2)
    if winner:
        return f"{winner.name} wins by playing {winner.hand}"
    else:
        return "It is a draw"