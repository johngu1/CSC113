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
    {"name": "Level 0: The Lobby", "description": "A seemingly endless beige expanse with a yellow-tinted lighting, the sound of a constant hum.", "monster": Entity('Skin-Stealer', 50, 15, 2)},
    {"name": "Level 1: The Halls", "description": "Winding corridors of the same dull, beige walls, with an occasional door leading to other levels.", "monster": Entity('Hounds', 30, 8, 3)},
    {"name": "Level 2: The Offices", "description": "A maze of cubicles and office spaces, with the occasional flicker of fluorescent lights.", "monster": Entity('Amalgam', 70, 12, 4)},
    {"name": "Level 3: The Kitchens", "description": "Large, industrial-style kitchens with long countertops and the faint smell of stale food.", "monster": Entity('Faceless', 40, 10, 6)},
    {"name": "Level 4: The Sewers", "description": "Dark, damp tunnels with the sound of dripping water and the occasional scurrying of unseen creatures.", "monster": Entity('Sewer Crawlers', 25, 6, 1)},
    {"name": "Level 5: The Emptiness", "description": "A vast, featureless void with no discernible walls or ceiling, the only sound being the echoes of your own footsteps.", "monster": Entity('The Watcher', 80, 18, 8)},
    {"name": "Level 6: The Suburbs", "description": "Rows of identical, abandoned houses with overgrown yards and the occasional flickering streetlight.", "monster": Entity('The Suburban Entity', 60, 14, 3)},
    {"name": "Level 7: The Hotel", "description": "A massive, dilapidated hotel with a grand lobby and long, winding corridors leading to countless rooms.", "monster": Entity('The Bellhop', 45, 12, 7)},
    {"name": "Level 8: The Wilderness", "description": "A dense, tangled forest with twisted, gnarled trees and the distant sounds of unknown creatures.", "monster": Entity('Wendigo', 90, 16, 5)},
    {"name": "Level 9: The Abyss", "description": "An endless, dark chasm with no visible bottom, the air filled with an unearthly howling.", "monster": Entity('The Unseen', 75, 20, 10)},
    {"name": "Level 10: The Megaplex", "description": "A sprawling, neon-lit complex of theaters, arcades, and abandoned stores, the air thick with the stale smell of popcorn.", "monster": Entity('The Entertainer', 55, 13, 4)}
]

@app.route('/')
def index():
    if 'player' not in session:
        session['player'] = vars(player)
    return render_template('index.html', player=session['player'], backrooms_levels=backrooms_levels)

@app.route('/explore', methods=['GET', 'POST'])
def explore():
    if request.method == 'POST':
        action = request.form['action']
        current_level = random.choice(backrooms_levels)
        monster = current_level['monster']
        player = Entity(**session['player'])

        if action == 'attack':
            player.health -= max(monster.attack - player.defense, 0)
            monster.health -= max(player.attack - monster.defense, 0)
        elif action == 'defend':
            player.defense += 2
        elif action == 'block':
            player.defense += 5

        session['player'] = vars(player)

        if player.health <= 0:
            return render_template('game_over.html')
        elif monster.health <= 0:
            return render_template('explore.html', level=current_level, player=session['player'])
        else:
            return render_template('explore.html', level=current_level, player=session['player'])

    return render_template('explore.html')

if __name__ == '__main__':
    app.run(debug=True)