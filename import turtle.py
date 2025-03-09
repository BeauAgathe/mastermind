import turtle
t= turtle.Pen()
t.color(0,1,1)
t.begin_fill()
t.circle(100)
t.end_fill()


boutton_cercle1 = tk.Button(racine, fill="red" )
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

def fill_circles(colors):
    for i in range(6):
        button=tk.Button(row=i, column=3, fill_color=colors[i])