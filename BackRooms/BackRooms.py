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
    print("You move north.")

def move_south():
    print("You move south.")

def move_east():
    print("You move east.")

def move_west():
    print("You move west.")

def look_around():
    print("You look around.")

def take_item():
    print("You take an item.")

def use_item():
    print("You use an item.")

def show_inventory():
    print("Your inventory is empty.")

# Define a route for each button press
@app.route("/button/<button>")
def button_pressed(button):
    # Call the corresponding function based on the button press
    buttons[button]()
    return "Button pressed!"

# Test the app
if __name__ == "__main__":
    app.run(debug=True)