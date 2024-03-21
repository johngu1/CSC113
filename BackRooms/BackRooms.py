from flask import Flask, render_template, request
import random

app = Flask(__name__)

# List of Backrooms level descriptions and monsters
backrooms_levels = [
    {"name": "Level 0: The Lobby", "description": "A seemingly endless beige expanse with a yellow-tinted lighting, the sound of a constant hum.", "monster": "Skin-Stealer"},
    {"name": "Level 1: The Halls", "description": "Winding corridors of the same dull, beige walls, with an occasional door leading to other levels.", "monster": "Hounds"},
    {"name": "Level 2: The Offices", "description": "A maze of cubicles and office spaces, with the occasional flicker of fluorescent lights.", "monster": "Amalgam"},
    {"name": "Level 3: The Kitchens", "description": "Large, industrial-style kitchens with long countertops and the faint smell of stale food.", "monster": "Faceless"},
    {"name": "Level 4: The Sewers", "description": "Dark, damp tunnels with the sound of dripping water and the occasional scurrying of unseen creatures.", "monster": "Sewer Crawlers"},
    {"name": "Level 5: The Emptiness", "description": "A vast, featureless void with no discernible walls or ceiling, the only sound being the echoes of your own footsteps.", "monster": "The Watcher"},
    {"name": "Level 6: The Suburbs", "description": "Rows of identical, abandoned houses with overgrown yards and the occasional flickering streetlight.", "monster": "The Suburban Entity"},
    {"name": "Level 7: The Hotel", "description": "A massive, dilapidated hotel with a grand lobby and long, winding corridors leading to countless rooms.", "monster": "The Bellhop"},
    {"name": "Level 8: The Wilderness", "description": "A dense, tangled forest with twisted, gnarled trees and the distant sounds of unknown creatures.", "monster": "Wendigo"},
    {"name": "Level 9: The Abyss", "description": "An endless, dark chasm with no visible bottom, the air filled with an unearthly howling.", "monster": "The Unseen"},
    {"name": "Level 10: The Megaplex", "description": "A sprawling, neon-lit complex of theaters, arcades, and abandoned stores, the air thick with the stale smell of popcorn.", "monster": "The Entertainer"}
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