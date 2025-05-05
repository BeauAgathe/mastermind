'''main'''

import tkinter as tk
import random as rd
import json
from pathlib import Path
from tkinter import messagebox
import math

# les couleurs qu'on peut utiliser dans le jeu:
red = "#EF476F"
yellow = "#FFD166"
green = "#06D6A0"
blue = "#118AB2"
white = "beige"
black = "#073B4C"

colors = [red, yellow, green, blue, black, white]

# création de la fenêtre de jeu
root = tk.Tk()
root.title("Mastermind")
root.geometry("550x750")
bg = tk.PhotoImage(file="photo/wood.png")
label1 = tk.Label(root, image=bg)
label1.place(x=0, y=0, relwidth=1, relheight=1)

# variables de jeu
nbr_couleurs=4
nbr_essaies=10
canvas = []
empty_circles = []
clicked_colors = []
current_canva = 0
current_circle = 0
mode = 1
GAGNE = False

# reinitialisation des colonnes de l'interface
root.columnconfigure(0, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)

#############################################################################
# fonctions pour l'interface


def create_canvas(root):
    '''fabrique les 10 canvas avec les emplacements dedans'''
    global nbr_couleurs, nbr_essaies
    global circles, canvas
    circles = []
    canvas = []
    for i in range(1, nbr_essaies+1):
        canva = tk.Canvas(root, width=325, height=50, bg="#d78a4e")
        canva.grid(row=i, column=2, pady=5)
        canvas.append(canva)
        for j in range(nbr_couleurs):
            center_x = 50 + 60*j
            center_y = 25
            circle = draw_cercle(center_x, center_y, canva, '#e5b38c')
            circles.append(circle)
        empty_circles.append(circles)


def draw_cercle(center_x, center_y, canva, color):
    """dessine un cercle sur le canva"""
    return canva.create_oval(center_x + 20, center_y + 20,
                             center_x - 20, center_y - 20, outline="#59230f",
                             fill=color)


def create_buttons():
    '''crée les boutons pour chaque couleur'''
    for i, color in enumerate(colors):
        button = tk.Button(root, bg=color, width=5, height=4,
                           command=lambda c=color: change_color_circle(c))
        button.grid(row=i+1, column=4)


def create_texte():
    '''pour créer un label qui affiche les textes'''
    global label
    label = tk.Label(root, text="")
    label.grid(column=5, row=1, rowspan=8)


def display_text(texte):
    '''change le texte dans le label'''
    label.configure(text=texte)

###############################################################################
# fonction pour le deroulement de la partie


def change_color_circle(coulor_button):
    '''quand on clique sur un boutton ça change la couleur du cercle'''
    global current_canva, current_circle,nbr_couleurs, nbr_essaies
    if len(clicked_colors) < nbr_couleurs:
        clicked_colors.append(coulor_button)
    if current_canva < nbr_essaies and current_circle < nbr_couleurs:
        canva = canvas[current_canva]
        canva.itemconfig(empty_circles[current_canva][current_circle],
                         fill=clicked_colors[-1])
        # clicked colors est une liste des couleur du code du joueur qui
        # se remplit au fur et a mesure du choix des couleurs.
        current_circle += 1


def compare_codes(guess, secret):
    """Compare le code du joueur avec le code secret(compare la position)"""
    correct_positions = sum([1 for i in range(nbr_couleurs) if guess[i] == secret[i]])
# va rajouter 1 a chaque qu'une couleur est dans la bonne position.
    misplaced_positions = 0
    secret_copy = secret[:]
    guess_copy = guess[:]
    for i in range(nbr_couleurs):
        if guess[i] == secret[i]:
            secret_copy[i] = None
            guess_copy[i] = None
            found_positions[i] = guess[i]
            if guess[i] not in found_colors:
                found_colors.append(guess[i])
    for color in guess_copy:
        if color and color in secret_copy:
            misplaced_positions += 1
            secret_copy[secret_copy.index(color)] = None
            if color not in found_colors:
                found_colors.append(color)
    return correct_positions, misplaced_positions


def display_feedback(correct, misplaced, row):
    '''rouge=bonne couleur et emplacement; blanc=bonne couleur'''
    feedback_canvas = tk.Canvas(root, width=100, height=50, bg="#d78a4e")
    feedback_canvas.grid(row=row+1, column=3)
    for i in range(correct):
        feedback_canvas.create_oval(10 + i * 20, 10, 30 + i * 20, 30,
                                    fill="red")
    for i in range(misplaced):
        feedback_canvas.create_oval(10 + (correct + i) * 20, 10,
                                    30 + (correct + i) * 20, 30, fill="white")


# fonction qui commence une nouvelle partie
def new_game():
    '''on réinitialise la fenêtre et
    recommence une partie avec nouveau code secret'''
    global GAGNE, code_secret, chosen_secret_code
    GAGNE = False
    if mode == 1:
        code_secret = create_secret_code()
    if mode == 2:
        code_secret = chosen_secret_code
    global canvas, empty_circles, clicked_colors, liste_feedbacks
    global current_canva, current_circle, tentatives, bg, label1
    canvas = []
    empty_circles = []
    clicked_colors = []
    current_canva = 0
    current_circle = 0
    tentatives = []
    liste_feedbacks = []
    for widget in root.winfo_children():
        widget.destroy()
    bg = tk.PhotoImage(file="photo/wood.png")
    label1 = tk.Label(root, image=bg)
    label1.place(x=0, y=0, relwidth=1, relheight=1)
    create_canvas(root)
    create_buttons()
    sauvegarder = tk.Button(root, text="Sauvegarder la partie",
                            command=save, bg='#e5b38c')
    sauvegarder.grid(column=2, row=nbr_essaies+2)
    global found_positions, found_colors
    found_positions = [None, None, None, None]
    found_colors = []
    hint = tk.Button(root, text="aide", command=help_me, bg='#e5b38c')
    hint.grid(column=4, row=12)
    global restart_image, back_image, check_image, home_image
    restart_image = tk.PhotoImage(file="photo/replay2.png")
    button_restart = tk.Button(root, image=restart_image, borderwidth=0,
                               command=new_game, bg='#e5b38c')
    button_restart.grid(row=9, column=4)
    back_image = tk.PhotoImage(file="photo/goback2.png")
    button_back = tk.Button(root, image=back_image, borderwidth=0,
                            command=back, bg='#e5b38c')
    button_back.grid(row=7, column=4)
    check_image = tk.PhotoImage(file="photo/done2.png")
    check_button = tk.Button(root, image=check_image, borderwidth=0,
                             command=check, bg='#e5b38c')
    check_button.grid(row=8, column=4)
    home_image = tk.PhotoImage(file="photo/home.png")
    check_button = tk.Button(root, image=home_image, borderwidth=0,
                             command=back_main_menu, bg='#e5b38c')
    check_button.grid(row=10, column=4)
    if GAGNE is True:
        return None
    if current_canva == len(canvas) and GAGNE is False:
        return None


###############################################################################
# fonctions pour les differentes options du jeu


def back():
    """Fonction qui permet de retourner en arriere"""
    global clicked_colors, current_circle, canvas
    if not clicked_colors:
        return None
    else:
        clicked_colors.pop()
        current_circle -= 1
        canvas[current_canva].itemconfig(empty_circles[current_canva][current_circle],
                                         fill="#e5b38c")


def check():
    '''va envoyer le feedback et passer au canva suivant'''
    global current_circle, clicked_colors, correct_positions, tentatives
    global misplaced_positions, current_canva, code_secret
    if current_circle == 4:
        tentatives.append(clicked_colors[:])
        correct_positions, misplaced_positions = compare_codes(clicked_colors, code_secret)
        feedback = [correct_positions, misplaced_positions]
        liste_feedbacks.append(feedback[:])
        display_feedback(correct_positions, misplaced_positions, current_canva)
        if correct_positions == nbr_couleurs:
            global GAGNE
            GAGNE = True
            end_game()
        elif current_canva == nbr_essaies-1:
            end_game()
            current_canva = 0
            clicked_colors.clear()
            current_circle = 0
            return None
        current_canva += 1
        clicked_colors.clear()
        current_circle = 0


def save():
    '''pour mettre la partie sous forme de dico et l'enregistrer'''
    dico = {}
    dico["mode"] = mode
    dico["GAGNE"] = GAGNE
    dico["code secret"] = code_secret
    dico["nombre d'essais"] = current_canva
    dico["tentatives"] = tentatives
    dico["couleurs trouvées"] = found_colors
    dico["positions trovées"] = found_positions
    dico["cercles vides"] = empty_circles
    dico["liste des feedbacks"] = liste_feedbacks
    sauvegarder_partie(dico)
    return None


def sauvegarder_partie(partie):
    '''pour enregistrer la partie dans le fichier'''
    nom_fichier = "sauvegarde_mastermind.json"
    with open(nom_fichier, "w") as f:
        json.dump(partie, f, indent=4)


def charger_partie(nom_fichier="sauvegarde_mastermind.json"):
    '''pour lancer la partie enregistrée'''
    try:
        with open(nom_fichier, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None


def affiche_ancienne_partie(partie):
    '''va afficher la partie enregistrée sur les canvas'''
    global mode, code_secret, GAGNE, current_canva, tentatives
    global found_positions, found_colors, empty_circles, liste_feedbacks
    liste_feedbacks = partie["liste des feedbacks"]
    mode = partie["mode"]
    code_secret = partie["code secret"]
    GAGNE = partie["GAGNE"]
    current_canva = partie["nombre d'essais"]
    tentatives = partie["tentatives"]
    found_positions = partie["positions trovées"]
    found_colors = partie["couleurs trouvées"]
    empty_circles = partie["cercles vides"]
    create_saved_canvas(tentatives, liste_feedbacks)
    create_buttons()
    sauvegarder = tk.Button(root, text="Sauvegarder la partie",
                            command=save, bg='#e5b38c')
    sauvegarder.grid(column=2, row=nbr_essaies+2)
    hint = tk.Button(root, text="aide", command=help_me, bg='#e5b38c')
    hint.grid(column=4, row=12)
    global restart_image, back_image, check_image, home_image
    restart_image = tk.PhotoImage(file="photo/replay2.png")
    button_restart = tk.Button(root, image=restart_image, borderwidth=0,
                               command=newww, bg='#e5b38c')
    button_restart.grid(row=9, column=4)
    back_image = tk.PhotoImage(file="photo/goback2.png")
    button_back = tk.Button(root, image=back_image, borderwidth=0,
                            command=back, bg='#e5b38c')
    button_back.grid(row=7, column=4)
    check_image = tk.PhotoImage(file="photo/done2.png")
    check_button = tk.Button(root, image=check_image, borderwidth=0,
                             command=check, bg='#e5b38c')
    check_button.grid(row=8, column=4)
    home_image = tk.PhotoImage(file="photo/home.png")
    check_button = tk.Button(root, image=home_image, borderwidth=0,
                             command=back_main_menu, bg='#e5b38c')
    check_button.grid(row=10, column=4)
    if GAGNE is True:
        return None
    if current_canva == nbr_essaies and GAGNE is False:
        return None

def newww():
    if mode == 1:
        new_game()
        return None
    if mode == 2:
        mode_2_players()
        return None  
    
def create_saved_canvas(tentatives, liste_feedbacks):
    '''pour chaque tentative, on colorie les cercles du canva'''
    global circles, canvas
    circles = []
    canvas = []
    for i in range(current_canva):
        canva = tk.Canvas(root, width=350, height=50, bg="#d78a4e")
        canva.grid(row=i+1, column=2, pady=5)
        canvas.append(canva)
        for h in range(nbr_couleurs):
            color = tentatives[i][h]
            center_x = 50 + 60*h
            center_y = 25
            circle = draw_cercle(center_x, center_y, canva, color)
            circles.append(circle)
        empty_circles.append(circles)
        display_feedback(liste_feedbacks[i][0], liste_feedbacks[i][1], i)
    for k in range(current_canva + 1, nbr_essaies+1):
        canva = tk.Canvas(root, width=350, height=50, bg="#d78a4e")
        canva.grid(row=k, column=2, pady=5)
        canvas.append(canva)
        for j in range(nbr_couleurs):
            center_x = 50 + 60*j
            center_y = 25
            circle = draw_cercle(center_x, center_y, canva, "#e5b38c")
            circles.append(circle)
        empty_circles.append(circles)


def help_me():
    '''renvoit un code qui marche avec les infos trouvées par le joueur'''
    hint = [None, None, None, None]
    if len(found_colors)==0 and len(found_positions)==0:
        return None
    for i in range(nbr_couleurs):
        if found_positions[i] is None:
            n = rd.randint(0, len(found_colors)-1)
            hint[i] = found_colors[n]
        else:
            hint[i] = found_positions[i]
    for i in range(nbr_couleurs):
        color = hint[i]
        if color == "#EF476F":
            hint[i] = "rouge"
        if color == "#FFD166":
            hint[i] = "jaune"
        if color == "#06D6A0":
            hint[i] = "vert"
        if color == "#118AB2":
            hint[i] = "bleu"
        if color == "beige":
            hint[i] = "blanc"
        if color == "#073B4C":
            hint[i] = "noir"
    str_hint = "Vous pouvez essayer le code: " + str(hint)
    messagebox.showinfo("Aide", str_hint)    #pris de ChatGPT


def change_color_secret(coulor_button):
    '''quand on clique sur un boutton ça change la couleur du cercle'''
    global current_circle
    clicked_colors.append(coulor_button)
    if current_circle < nbr_couleurs:
        canva_secret.itemconfig(cercles2[current_circle],
                                fill=clicked_colors[-1])
        current_circle += 1
    global chosen_secret_code
    chosen_secret_code = clicked_colors


def choose_secret_code():
    '''le deuxieme utilisateur va choisir un code secret'''
    global window_code
    window_code = tk.Tk()
    window_code.title("CHOISIR CODE SECRET")
    window_code.configure(bg='#e5b38c')
    global canva_secret, clicked_colors, current_circle, vide_circles, cercles2
    cercles2 = []
    vide_circles = [None, None, None, None]
    clicked_colors = []
    current_circle = 0
    canva_secret = tk.Canvas(window_code, width=400, height=80, bg = '#d78a4e')
    canva_secret.pack(pady=20)
    for i in range(nbr_couleurs):
        cercle = canva_secret.create_oval(50 + i * 80, 20, 90 + i * 80, 60,
                                          outline="#59230f", width=2,
                                          fill="#e5b38c")
        cercles2.append(cercle)
    for couleur in colors:
        boutton = tk.Button(window_code, text='        ', bg=couleur,
                            command=lambda c=couleur: change_color_secret(c))
        boutton.pack(side=tk.LEFT, padx=5)

    enregistrer_button = tk.Button(window_code,
                                   text="Enregistrer Code Secret",
                                   command=lambda: [window_code.destroy(), new_game()], bg = '#d78a4e', fg = '#59230f')
    enregistrer_button.pack(pady=10)
    window_code.mainloop()
    if len(clicked_colors) == nbr_couleurs:
        return clicked_colors


def create_secret_code():
    '''fabrique aléatoirement un code couleur à deviner'''
    The_secret_code = []
    while len(The_secret_code) < nbr_couleurs:
        The_secret_code.append(colors[rd.randint(0, 5)])
    return The_secret_code


def mode_1_player():
    '''l'ordi cree un code secret que le joueur doit deviner'''
    global mode
    mode = 1
    new_game()


def mode_2_players():
    '''un joueur choisi le code secret et un autre joueur le devine'''
    global mode, chosen_secret_code
    mode = 2
    chosen_secret_code = choose_secret_code()
    new_game()


def end_game():  
    '''la partie est terminée'''
    dialog = tk.Toplevel(root)    #pris de ChatGPT
    dialog.title("Partie terminée !")
    dialog.geometry("500x200")
    dialog.configure(bg='#d78a4e')
    label = tk.Label(dialog, text="La partie est terminée.",
                     font=("Times New Roman", 12), bg ='#e5b38c', fg = '#59230f')
    label.pack(pady=20)
    if GAGNE is True:
        labelg = tk.Label(dialog, text="BRAVOO! Vous avez gagné!",
                          font=("Times New Roman", 15), bg = '#e5b38c', fg = '#59230f')
        labelg.pack(pady=15)
        fireworks()
    else:
        labelf = tk.Label(dialog, text="Vous avez perdu", font=("Times New Roman", 15), bg = '#59230f')
        labelf.pack(pady=15)
    button_frame = tk.Frame(dialog, bg ='#d78a4e' )
    button_frame.pack(pady=10)
    replay_button = tk.Button(button_frame, text="Rejouer", width=10,
                              command=lambda: [dialog.destroy(), mode_2_players()], bg = '#e5b38c')   #pris de chatGPT
    replay_button.pack(side="left", padx=10)
    back_button = tk.Button(button_frame, text="Menu principal", width=15,
                            command=lambda: [dialog.destroy(), back_main_menu()], bg = '#e5b38c')
    back_button.pack(side="right", padx=10)
    nom_fichier = Path("sauvegarde_mastermind.json")
    nom_fichier.unlink()



def fireworks(): #By chatGPT
    canvas = tk.Canvas(root, width=root.winfo_width(), height=root.winfo_height(),
                       highlightthickness=0, bg="#e5b38c", bd=0)
    canvas.place(x=0, y=0)

    explosions = []

    for _ in range(24):  # Trois feux d'artifice
        cx = rd.randint(100, root.winfo_width() - 100)
        cy = rd.randint(100, root.winfo_height() // 2)
        color = rd.choice(["red", "blue", "yellow", "orange", "purple", "cyan", "lime"])
        particles = []

        for angle in range(0, 360, 15):
            radians = math.radians(angle)
            dx = math.cos(radians) * 2
            dy = math.sin(radians) * 2
            dot = canvas.create_oval(cx, cy, cx+4, cy+4, fill=color, outline="")
            particles.append((dot, dx, dy))

        explosions.append(particles)

    def animate():
        for particles in explosions:
            for dot, dx, dy in particles:
                canvas.move(dot, dx, dy)
        root.after(20, animate)

    animate()

    # Supprimer après 2.5 secondes
    root.after(5000, canvas.destroy)



def back_main_menu():
    '''retour au menu principal'''
    global Mastermind_image, bg  # garder ref image pour pas avoir garbage
    for widget in root.winfo_children():
        widget.destroy()

    bg = tk.PhotoImage( file = "photo/wood.png")
    label1 = tk.Label( root, image = bg) 
    label1.place(x = 0,y = 0, relwidth=1, relheight=1)
    mode1 = tk.Button(root, text="One Player Mode", command=mode_1_player, bg = '#d78a4e', fg = '#59230f')
    mode1.place(relx=0.40, rely=0.55)
    mode2 = tk.Button(root, text="Two Player Mode", command=mode_2_players, bg = '#d78a4e', fg = '#59230f')
    mode2.place(relx=0.40, rely=0.60)
    border_color = tk.Frame(root, background="#d78a4e")
    label = tk.Label(border_color, text="Mastermind", font= ('Times New Roman', 50 , 'bold'), bd=0, bg = '#59230f' , fg = '#d78a4e')
    label.pack(padx=1, pady=1)
    border_color.pack(padx=40, pady=275)



partie = charger_partie()
if partie is not None:
    affiche_ancienne_partie(partie)
if partie is None:
    mode1 = tk.Button(root, text="One Player Mode", command=mode_1_player, bg = '#d78a4e', fg = '#59230f')
    mode1.place(relx=0.40, rely=0.55)
    mode2 = tk.Button(root, text="Two Players Mode", command=mode_2_players, bg = '#d78a4e', fg = '#59230f')
    mode2.place(relx=0.40, rely=0.60)
    border_color = tk.Frame(root, background="#d78a4e")
    label = tk.Label(border_color, text="Mastermind", font= ('Times New Roman', 50 , 'bold'), bd=0, bg = '#59230f' , fg = '#d78a4e')
    label.pack(padx=1, pady=1)
    border_color.pack(padx=40, pady=275)

root.mainloop()

#De temps en temps, on a eu de l'aide de L'oncle de Khaola, frere de Agathe et ChatGPT.