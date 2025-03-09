'''interface'''

import tkinter as tk
import random as rd


# nouvelle fenêtre racine
racine = tk.Tk()
racine.title("Mastermind")
racine.geometry("1200x700")

canva=tk.Canvas(racine, width =400 , height = 50, bg="saddlebrown" )
canva.grid(row=1, column=2)
canva=tk.Canvas(racine, width =400 , height = 50, bg="saddlebrown" )
canva.grid(row=2, column=2)
canva=tk.Canvas(racine, width =400 , height = 50, bg="saddlebrown" )
canva.grid(row=3, column=2)
canva=tk.Canvas(racine, width =400 , height = 50, bg="saddlebrown" )
canva.grid(row=4, column=2)
canva=tk.Canvas(racine, width =400 , height = 50, bg="saddlebrown" )
canva.grid(row=5, column=2)
canva=tk.Canvas(racine, width =400 , height = 50, bg="saddlebrown" )
canva.grid(row=6, column=2)



white = (200, 200, 200)
black = (30, 30, 30)
green = (0, 210, 0)
blue= (0, 0, 200)
red = (210, 0, 0)
yellow = (210, 210, 0)
colors=(white,black, green, blue, red, yellow )
def draw_button()->None:
    center_x=rd.randint(10,700-50)
    center_y=rd.randint(10,1200-50)
    canva.create_oval(center_x-50,center_y+50,center_x+50,center_y-50,)
for i in range(6):
    button_cercle=tk.Button(racine, command=draw_button(), bg=colors)
    button_cercle.grid(row=i, column=3, bg=colors)


boutton_cercle1 = tk.Button(racine, commande=draw_button(), bg='white')
boutton_cercle1.grid(row=1, column=3)
boutton_cercle2 = tk.Button(racine, command=draw_button(),bg='black')
boutton_cercle2.grid(row=2, column=3)
boutton_cercle3 = tk.Button(racine, command=draw_button(), bg='red')
boutton_cercle3.grid(row=3, column=3)
boutton_cercle4 = tk.Button(racine, command=draw_button(), bg='green')
boutton_cercle4.grid(row=4, column=3)
boutton_cercle5 = tk.Button(racine, command=draw_button(),bg='yellow')
boutton_cercle5.grid(row=5, column=3)
boutton_cercle6 = tk.Button(racine, command=draw_button(), bg='blue')
boutton_cercle6.grid(row=6, column=3)


racine.mainloop()


#test
