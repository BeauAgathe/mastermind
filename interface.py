'''interface'''

import tkinter as tk
# nouvelle fenêtre racine
racine = tk.Tk()
racine.title("Mastermind")
racine.geometry("1200x700")

canva=tk.Canvas(racine, width =400 , height = 50, bg="pink" )
canva.grid(row=0, column=2)
canva=tk.Canvas(racine, width =400 , height = 50, bg="pink" )
canva.grid(row=1, column=2)
canva=tk.Canvas(racine, width =400 , height = 50, bg="pink" )
canva.grid(row=2, column=2)
canva=tk.Canvas(racine, width =400 , height = 50, bg="pink" )
canva.grid(row=3, column=2)
canva=tk.Canvas(racine, width =400 , height = 50, bg="pink" )
canva.grid(row=4, column=2)
canva=tk.Canvas(racine, width =400 , height = 50, bg="pink" )
canva.grid(row=5, column=2)

boutton_cercle1 = tk.Button(racine, fill="red")
boutton_cercle1.grid(row=0, column=3)
boutton_cercle2 = tk.Button(racine, fill="blue")
boutton_cercle2.grid(row=1, column=3)
boutton_cercle3 = tk.Button(racine, fill="yellow")
boutton_cercle3.grid(row=2, column=3)
boutton_cercle4 = tk.Button(racine, fill="black")
boutton_cercle4.grid(row=3, column=3)
boutton_cercle5 = tk.Button(racine, fill="white")
boutton_cercle5.grid(row=4, column=3)
boutton_cercle6 = tk.Button(racine, fill="green")
boutton_cercle6.grid(row=5, column=3)



racine.mainloop()


#test
