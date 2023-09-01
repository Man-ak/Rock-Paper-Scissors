from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    player_choice = request.form['choice']
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    # Define winning conditions
    winning_conditions = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }

    # Determine the winner
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif winning_conditions[player_choice] == computer_choice:
        result = "You win!"
    else:
        result = "You lose!"

    return render_template('results.html', player=player_choice, computer=computer_choice, result=result)

if __name__ == "__main__":
    app.run(debug=True)
