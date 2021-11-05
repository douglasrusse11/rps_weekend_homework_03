from app import app
from models.run_game import run_game
from flask import render_template

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/<hand1>/<hand2>')
def rps(hand1, hand2):
    winner = run_game(hand1, hand2)
    if winner:
        return render_template("winner.html", winner_string=f"{winner.name} wins by playing {winner.hand}")
    else:
        return render_template("winner.html", winner_string="It is a draw")