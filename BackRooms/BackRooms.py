from flask import Flask, render_template, request
import random
app = Flask(__name__)

# Define a dictionary to map buttons to their corresponding actions
buttons = {
    "n": "move_north",
    "s": "move_south",
    "e": "move_east",
    "w": "move_west",
    "look": "look_around",
    "take": "take_item",
    "use": "use_item",
    "inventory": "show_inventory"
}

# Define a function for each button action
def move_north():
    return "You move north."

def move_south():
    return "You move south."

def move_east():
    return "You move east."

def move_west():
    return "You move west."

def look_around():
    return "You look around."

def take_item():
    return "You take an item."

def use_item():
    return "You use an item."

def show_inventory():
    return "Your inventory is: "

# Define a function to handle user input and execute the corresponding action
def handle_input(input_):
    input_ = input_.lower()
    if input_ in buttons:
        return buttons[input_]()
    else:
        return "Invalid input. Type 'help' for a list of available commands."

# Define a function to generate a random room and items
def generate_room():
    room = random.choice(["Forest", "Dungeon", "Cave", "Tavern"])
    items = []
    for i in range(random.randint(1, 3)):
        items.append(random.choice(["Sword", "Potion", "Key", "Map"]))
    return room, items

# Define a function to print the room and items
def print_room(room, items):
    print(f"You are in a {room}.")
    for item in items:
        print(f"You see a {item}.")

# Define a route for the root URL
@app.route("/")
def index():
    return render_template("index.html")

# Define a route for the game
@app.route("/game")
def game():
    room, items = generate_room()
    user_input = request.args.get("input")
    if user_input:
        handle_input(user_input)
    return render_template("game.html", room=room, items=items)

# Define a route for the inventory
@app.route("/inventory")
def inventory():
    return render_template("inventory.html")

# Define a route for the help page
@app.route("/help")
def help():
    return render_template("help.html")

# Define a route for the about page
@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run()