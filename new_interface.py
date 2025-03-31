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


def draw_empty_circle(x, y, rayon, canva):
    """Dessine un cercle vide dans le canva"""
    return canva.create_oval(x - rayon, y - rayon, x + rayon, y + rayon, outline="purple", width=2)

def setup():
    """Cree les canavas"""
    global canvas, empty_circles, clicked_colors, current_canva, current_circle
    canvas = []
    empty_circles = []
    clicked_colors = []
    current_canva = 0
    current_circle = 0
    for widget in racine.winfo_children(): #prend tout les widget dans racine.(boutons, canvas...)
        widget.destroy()#supprime les widget de la fenetre.
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
    """Cree les boutons de couleur"""
    for i, color in enumerate(colors): #parcourie la liste couleurs en associaint a chaque element son indice.(sa position dans la liste.)
        button = tk.Button(racine, bg=color, command=lambda c=color: changer_couleur_cercle(c))
        button.grid(row=i+1, column=4) 

def changer_couleur_cercle(couleur_boutton):
    global current_canva, current_circle
    if len(clicked_colors) < 4:
        clicked_colors.append(couleur_boutton)
    if current_canva < len(canvas):
        canva = canvas[current_canva]
        canva.itemconfig(empty_circles[current_canva][current_circle], fill=clicked_colors[-1])# clicked colors est une liste des couleur du code du joueru qui se remplit au fur et a mesure du choix des couleurs.
        #changer les proprietes du premier cercle dans le premier canva puis passer au suivant.
        current_circle += 1
        if current_circle == 4:
            correct_positions, misplaced_positions = comparer_codes(clicked_colors, secret_code)
            display_feedback(correct_positions, misplaced_positions, current_canva)
            if correct_positions == 4:
                print("You are a champion")
            elif current_canva == 9:
                print("Out of attemps, GAME OVER")
            current_canva += 1
            clicked_colors.clear()
            current_circle = 0 #recommence un nouveau essai dans le prochain canva.
  

def comparer_codes(guess, secret):
    """Compare le imput_code du jouer avec le code genere aleatoirement par le jeu(compare la couleur et la position)"""
    correct_positions = sum([1 for i in range(4) if guess[i] == secret[i]]) #va rajouter 1 a chaque qu'une couleur est dans la bonne position.
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
        feedback_canvas.create_oval(10 + i * 20, 10, 30 + i * 20, 30, fill="red") #le nombre de cercle rouge a tracer pour chaque couleur a la bonne position
    for i in range(misplaced):
        feedback_canvas.create_oval(10 + (correct + i) * 20, 10, 30 + (correct + i) * 20, 30, fill="white") #combine le nombre de cercle a la bonne position avec l'indice i du cercle du feedback.

def start_one_player_mode():
    """Le code secret est genere aleatoirement par le jeu, et le joueur doit le deviner"""
    global secret_code
    secret_code = [rd.choice(colors) for _ in range(4)]
    #print(secret_code)
    setup()


import tkinter as tk
racine = tk.Tk()
racine.title("Jeu Mastermind - Mode Deux Joueurs")


couleurs_disponibles = ['white', 'black', 'red', 'green', 'yellow', 'blue']

cercles=[]
canva = tk.Canvas(racine, width=400, height=80)
canva.pack(pady=20)


for i in range(4):
    cercle = canva.create_oval(50 + i * 80, 20, 90 + i * 80, 60, outline="black", width=2, fill="white")
    cercles.append(cercle)


boutons = tk.Button(racine)
boutons.pack(pady=10)


for couleur in couleurs_disponibles:
    couleur = tk.Button(boutons, text=couleur.capitalize(), bg=couleur, 
                               command=lambda couleur=couleur: couleur(couleur, couleurs.index()))
    couleur.pack(side=tk.LEFT, padx=5)


label_code_secret = tk.Label(racine, text="", font=( 14))
label_code_secret.pack(pady=10)


enregistrer_button = tk.Button(racine, text="Enregistrer Code Secret", )
enregistrer_button.pack(pady=10)


racine.mainloop()
