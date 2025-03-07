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
