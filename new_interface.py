'''interface'''

import tkinter as tk


# nouvelle fenêtre racine
def interface_du_mastermind():
    '''génère une nouvelle interface vide'''
    racine = tk.Tk()
    racine.title("Mastermind")
    racine.geometry("1200x700")
    create_canvas(racine)
    create_buttons(racine)
    racine.mainloop()
    return racine
   
'''interface'''

import tkinter as tk
import random as rd


# nouvelle fenêtre racine
racine = tk.Tk()
racine.title("Mastermind")
racine.geometry("1200x700")

canvas=[]
for i in range(6):
 canva=tk.Canvas(racine, width =400 , height = 100, bg="pink" )
 canva.grid(row=i+1, column=2)
 canvas.append(canva)


def draw_empty_circle(x, y, rayon, canva):
    """Draws an empty circle in canva"""
    return canva.create_oval(x - rayon, y - rayon, x + rayon, y + rayon, outline="purple", width=2)
x_beginning=50
y_cercle=40
space=80
empty_circles=[]
for canva in canvas:
   circles=[]
   for i in range(4):
    circle=draw_empty_circle(x_beginning+i*space, y_cercle, 30, canva)
    circles.append(circle)
    empty_circles.append(circles)
clicked_colors=[]
current_canva=0
current_circle=0
def change_couleur_cercle(couleur_boutton):
    global current_canva, current_circle
    if len(clicked_colors)<4:
       clicked_colors.append(couleur_boutton)
       if current_canva < len(canvas):
          canva=canvas[current_canva]
          canva.itemconfig(empty_circles[current_canva][current_circle], fill= clicked_colors[-1])
          current_circle+=1
          if current_circle==4:
            current_canva+=1 
            clicked_colors.clear()
            current_circle=0
            
boutton1 = tk.Button(racine, bg='white',command=lambda:change_couleur_cercle('white'))
boutton1.grid(row=1, column=3)
boutton2 = tk.Button(racine,bg='black', command=lambda:change_couleur_cercle('black'))
boutton2.grid(row=2, column=3)
boutton3 = tk.Button(racine,  bg='red', command=lambda:change_couleur_cercle('red'))
boutton3.grid(row=3, column=3)
boutton4 = tk.Button(racine, bg='green',command=lambda:change_couleur_cercle('green'))
boutton4.grid(row=4, column=3)
boutton5 = tk.Button(racine, bg='yellow',command=lambda:change_couleur_cercle('yellow'))
boutton5.grid(row=5, column=3)
boutton6 = tk.Button(racine, bg='blue', command=lambda:change_couleur_cercle('blue'))
boutton6.grid(row=6, column=3)



color_choices=['white','black','green','yellow','red','blue']
code_secret=[rd.choice(color_choices) for _ in range(4)]

tries= []
current_canva=0
def verification_color_code():
   global clicked_colors, current_circle, current_canva
   if len(clicked_colors)==4:
      tries.append(clicked_colors.copy())
   if clicked_colors==code_secret:
      label_message.config(text="CORRECT CODE, You're a champion", fg="green")
      return
   elif current_canva>len(canvas)-1:
      label_message.config(racine, text="GAME OVER!!! The correct answer was:"+str(code_secret))
   else:
      label_message.config(text="Try again, you got this", fg="red")

   clicked_colors.clear()
   current_circle=0
   



button_verification=tk.Button(racine, text="Verify",command=verification_color_code)   
button_verification.grid(row=7, column=3)   
label_message=tk.Label(racine, text="", font=(("Arial"),15))
label_message.grid(row=8, column=3)
      



racine.mainloop()


#test



# test 2






# les canvas roses où le joueur place son code
def create_canvas(racine):
    '''fabrique les 12 canvas avec les emplacements dedans'''
    for i in range(12):
        canva = tk.Canvas(racine, width=350, height=50, bg="pink")
        canva.grid(row=i, column=2)
        for j in range(5):
            centre_x = 50 + 60*j
            centre_y = 25
            canva.create_oval(centre_x + 15, centre_y + 15,
                              centre_x - 15, centre_y - 15, outline="white")


# les boutons qui génèrent les couleures pour le code cu joueur
def create_buttons(racine):
    '''fabrique les boutons pour chaque couleur'''
    boutton_cercle1 = tk.Button(racine, text="rouge", font="red")
    boutton_cercle1.grid(row=0, column=3)
    boutton_cercle2 = tk.Button(racine, text="bleu", font="blue")
    boutton_cercle2.grid(row=1, column=3)
    boutton_cercle3 = tk.Button(racine, text="jaune", font="yellow")
    boutton_cercle3.grid(row=2, column=3)
    boutton_cercle4 = tk.Button(racine, text="noir", font="black")
    boutton_cercle4.grid(row=3, column=3)
    boutton_cercle5 = tk.Button(racine, text="blanc", font="white")
    boutton_cercle5.grid(row=4, column=3)
    boutton_cercle6 = tk.Button(racine, text="vert", font="green")
    boutton_cercle6.grid(row=5, column=3)

###############################################################################################
import tkinter as tk
import random as rd

# nouvelle fenêtre racine
racine = tk.Tk()
racine.title("Mastermind")
racine.geometry("1200x1000")

canvas = []
empty_circles = []
clicked_colors = []
current_canva = 0
current_circle = 0
secret_code = []

colors = ['white', 'black', 'red', 'green', 'yellow', 'blue']

def draw_empty_circle(x, y, rayon, canva):
    """Draws an empty circle in canva"""
    return canva.create_oval(x - rayon, y - rayon, x + rayon, y + rayon, outline="black", width=2)

def setup():
    global canvas, empty_circles, clicked_colors, current_canva, current_circle
    canvas = []
    empty_circles = []
    clicked_colors = []
    current_canva = 0
    current_circle = 0
    for widget in racine.winfo_children():
        widget.destroy()
    for i in range(10):
        canva = tk.Canvas(racine, width=400, height=80, bg="pink")
        canva.grid(row=i+1, column=2)
        canvas.append(canva)
    x_beginning = 40
    y_cercle = 40
    space = 80
    for canva in canvas:
        circles = []
        for i in range(4):
            circle = draw_empty_circle(x_beginning + i * space, y_cercle, 30, canva)
            circles.append(circle)
        empty_circles.append(circles)
    create_color_buttons()

def create_color_buttons():
    for i, color in enumerate(colors):
        button = tk.Button(racine, bg=color, command=lambda c=color: change_couleur_cercle(c))
        button.grid(row=i+1, column=4)

def change_couleur_cercle(couleur_boutton):
    global current_canva, current_circle
    if len(clicked_colors) < 4:
        clicked_colors.append(couleur_boutton)
    if current_canva < len(canvas):
        canva = canvas[current_canva]
        canva.itemconfig(empty_circles[current_canva][current_circle], fill=clicked_colors[-1])# clicked colors est une liste des couleur du code du joueru qui se remplit au fur et a mesure du choix des couleurs.
        current_circle += 1
        if current_circle == 4:
            correct_positions, misplaced_positions = compare_codes(clicked_colors, secret_code)
            display_feedback(correct_positions, misplaced_positions, current_canva)
            if correct_positions == 4:
                print("You win!")
            elif current_canva == 9:
                print("Out of attempts!")
            current_canva += 1
            clicked_colors.clear()
            current_circle = 0

def compare_codes(guess, secret):
    correct_positions = sum([1 for i in range(4) if guess[i] == secret[i]])
    misplaced_positions = 0
    secret_copy = secret[:]
    guess_copy = guess[:]
    for i in range(4):
        if guess[i] == secret[i]:
            secret_copy[i] = None
            guess_copy[i] = None
    for color in guess_copy:
        if color and color in secret_copy:
            misplaced_positions += 1
            secret_copy[secret_copy.index(color)] = None
    return correct_positions, misplaced_positions

def display_feedback(correct, misplaced, row):
    feedback_canvas = tk.Canvas(racine, width=100, height=50, bg="pink")
    feedback_canvas.grid(row=row+1, column=3)
    for i in range(correct):
        feedback_canvas.create_oval(10 + i * 20, 10, 30 + i * 20, 30, fill="red")
    for i in range(misplaced):
        feedback_canvas.create_oval(10 + (correct + i) * 20, 10, 30 + (correct + i) * 20, 30, fill="white")

def start_one_player_mode():
    global secret_code
    secret_code = [rd.choice(colors) for _ in range(4)]
    #print(secret_code)
    setup()



def create_secret_code_input():
    input_canvas = tk.Canvas(racine, width=400, height=50, bg="pink")
    input_canvas.grid(row=0, column=2)
    input_circles = []
    for i in range(4):
        circle = draw_empty_circle(40 + i * 80, 25, 20, input_canvas)
        input_circles.append(circle)
    input_colors = []
    def set_secret_code(couleur_boutton):
        if len(input_colors) < 4:
            input_colors.append(couleur_boutton)
            input_canvas.itemconfig(input_circles[len(input_colors) - 1], fill=couleur_boutton)
        if len(input_colors) == 4:
            global secret_code
            secret_code = input_colors
            print("Secret code set:", secret_code)  # For debugging purposes
            input_canvas.destroy()
    for i, color in enumerate(colors):
        button = tk.Button(racine, bg=color, command=lambda c=color: set_secret_code(c))
        button.grid(row=i+1, column=5)

tk.Button(racine, text="Welcome to Mastermind", command=start_one_player_mode).grid(row=0, column=0)

racine.mainloop()
