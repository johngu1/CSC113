from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Player and monster stats
class Entity:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

player = Entity('Player', 100, 10, 5)

backrooms_levels = [
    # Your Backrooms level and monster data
]

@app.route('/')
def index():
    if 'player' not in session:
        session['player'] = vars(player)
    return render_template('index.html', player=session['player'], backrooms_levels=backrooms_levels)

@app.route('/play', methods=['GET', 'POST'])
def play():
    if request.method == 'POST':
        action = request.form['action']
        current_level = random.choice(backrooms_levels)
        monster = current_level['monster']
        player = Entity(**session['player'])

        # Your combat logic here

        session['player'] = vars(player)

        if player.health <= 0:
            return render_template('game_over.html')
        elif monster.health <= 0:
            return render_template('play.html', level=current_level, player=session['player'])
        else:
            return render_template('play.html', level=current_level, player=session['player'])

    return render_template('play.html')

if __name__ == '__main__':
    app.run(debug=True)