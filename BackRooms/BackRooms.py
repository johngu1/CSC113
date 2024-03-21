from flask import Flask, render_template, request
import random

app = Flask(__name__)

# List of Backrooms level descriptions
backrooms_levels = [
    "Level 0: The Lobby - A seemingly endless beige expanse with a yellow-tinted lighting, the sound of a constant hum.",
    "Level 1: The Halls - Winding corridors of the same dull, beige walls, with an occasional door leading to other levels.",
    "Level 2: The Offices - A maze of cubicles and office spaces, with the occasional flicker of fluorescent lights.",
    "Level 3: The Kitchens - Large, industrial-style kitchens with long countertops and the faint smell of stale food.",
    "Level 4: The Sewers - Dark, damp tunnels with the sound of dripping water and the occasional scurrying of unseen creatures.",
    "Level 5: The Emptiness - A vast, featureless void with no discernible walls or ceiling, the only sound being the echoes of your own footsteps."
    "Level 6: The Suburbs - Rows of identical, abandoned houses with overgrown yards and the occasional flickering streetlight.",
    "Level 7: The Hotel - A massive, dilapidated hotel with a grand lobby and long, winding corridors leading to countless rooms.",
    "Level 8: The Wilderness - A dense, tangled forest with twisted, gnarled trees and the distant sounds of unknown creatures.",
    "Level 9: The Abyss - An endless, dark chasm with no visible bottom, the air filled with an unearthly howling.",
    "Level 10: The Megaplex - A sprawling, neon-lit complex of theaters, arcades, and abandoned stores, the air thick with the stale smell of popcorn."
]

@app.route('/')
def index():
    return render_template('index.html', backrooms_levels=backrooms_levels)

@app.route('/explore', methods=['GET', 'POST'])
def explore():
    if request.method == 'POST':
        level = random.choice(backrooms_levels)
        return render_template('explore.html', level=level)
    return render_template('explore.html')

if __name__ == '__main__':
    app.run(debug=True)