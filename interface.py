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

#Les 6 canvas marrons
canvas=[]
for i in range(6):
 canva=tk.Canvas(racine, width =400 , height = 50, bg="saddlebrown" )
 canva.grid(row=i+1, column=2)
 canvas.append(canva)

# Fonction qui dessine les 4 cercles dans chaque canva.
def draw_empty_circle(x, y, rayon, canva):
    canva.create_oval(x - rayon, y - rayon, x + rayon, y + rayon, outline="black", width=2)
x_beginning=40
y_cercle=25
space=80

empty_circles=[]
for canva in canvas:
   circles=[]
   for i in range(4):
    circle=draw_empty_circle(x_beginning+i*space, y_cercle, 20, canva)
    circles.append(circle)
    empty_circles.append(circles)
clicked_colors=[]
def change_couleur_cercle(couleur_boutton):
    if len(clicked_colors)<4:
       clicked_colors.append(couleur_boutton)
       for i, canva in enumerate(canvas):
         for j, circle in enumerate(circles):
          for k in range(4):
            canva.itemconfig(empty_circles[i][j][k], fill= clicked_colors[i])
            #A revoir, cette fonction ne marche pas comme prevu.
  
  


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
