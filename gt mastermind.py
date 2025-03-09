import tkinter as tk
import random

def on_drag(event):
    widget = event.widget
    widget.place(x=event.x_root - widget.winfo_width() // 2 - root.winfo_x(),
                 y=event.y_root - widget.winfo_height() // 2 - root.winfo_y())

def check_guess():
    global attempts
    guess = [button_colors[i] for i in range(4)]
    if len(guess) != 4:
        return
    
    black_pegs, white_pegs = 0, 0
    secret_copy = secret_code[:]
    guess_copy = guess[:]
    
    # Check for exact matches (black pegs)
    for i in range(4):
        if guess[i] == secret_code[i]:
            black_pegs += 1
            secret_copy[i] = guess_copy[i] = None
    
    # Check for color matches (white pegs)
    for i in range(4):
        if guess_copy[i] and guess_copy[i] in secret_copy:
            white_pegs += 1
            secret_copy[secret_copy.index(guess_copy[i])] = None
    
    feedback_label.config(text=f"Black pegs: {black_pegs}, White pegs: {white_pegs}")
    attempts += 1
    if black_pegs == 4:
        feedback_label.config(text=f"Congratulations! You guessed the code in {attempts} attempts!")
    elif attempts >= max_attempts:
        feedback_label.config(text=f"Game Over! The code was {secret_code}")

# Create main window
root = tk.Tk()
root.title("Mastermind Game")

# Create a canvas
canvas = tk.Canvas(root, width=500, height=500, bg="white")
canvas.pack()

# Define colors
colors = ["white", "black", "green", "yellow", "red", "blue"]

# Generate a random secret code
secret_code = random.choices(colors, k=4)
print("Secret Code (for testing):", secret_code)

# Create draggable color buttons
button_colors = [None] * 4
for i, color in enumerate(colors):
    btn = tk.Button(root, bg=color, width=5, height=2)
    btn.place(x=50 + i * 60, y=400)
    btn.bind("<B1-Motion>", on_drag)
    if i < 4:
        button_colors[i] = color

# Submit button
guess_button = tk.Button(root, text="Submit Guess", command=check_guess)
guess_button.pack()

feedback_label = tk.Label(root, text="")
feedback_label.pack()

# Game parameters
attempts = 0
max_attempts = 10

# Run the Tkinter event loop
root.mainloop()
