from app import app
from models.run_game import run_game
from flask import render_template

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<hand1>/<hand2>')
def rps(hand1, hand2):
    winner, players_list = run_game(hand1, hand2)
    if winner == 404:
        return render_template("bam.html")
    elif winner:
        return render_template("winner.html", winner_string=f"{winner.name} wins by playing {winner.hand}", players=players_list)
    else:
        return render_template("winner.html", winner_string="It is a draw", players = players_list)