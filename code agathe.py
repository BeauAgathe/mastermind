'''agathe'''


def sauvegarder(nom_partie):
    '''pour enregistrer la partie dans le fichier'''
    sauv = open('fichier de sauvegarde', "a")
    dico = {"partie":nom_partie}
    if mode == 1:
        m = "un seul joueur"
    if mode == 2:
        m = "deux joueurs"
    dico["mode"] = m
    dico["code secret"] = code_secret
    if GAGNE is True:
        r = "victoire, le code secret a été deviné"
    if GAGNE is False:
        r = "défaite, le code secret n'a pas été deviné"
    dico["résulat"] = r
    dico["nombre d'essais"] = current_canva
    dico["tentatives"] = tentatives
    sauv.write(str(dico) + "\n")
    sauv.close()


def input():
    user_input = entry.get()
    label.config(text=f"You entered: {user_input}")


entry = tk.Entry(racine)
entry.grid(row=2, column=1)
button = tk.Button(racine, text="Submit", command=input)
button.grid(row=3, column=1)
label = tk.Label(racine, text="Nommer la partie")
label.grid(row=4, column=1)


def voir_vieilles_parties():
    '''pour regarder les infos des parties enregistrées'''
    fichier = open('fichier de sauvegarde', "r")
    past_games = []
    a = fichier.readline()
    while a != "":
        past_games.append(a)
        a = fichier.readline()
    fichier.close()
    affiche_texte(past_games)


def voir_vieilles_parties2():
    '''pour regarder les infos des parties enregistrées'''
    fichier = open('fichier de sauvegarde', "r")
    past_games = fichier.readlines()
    fichier.close()
    affiche_texte(past_games["parties"])


def sauvegarder(nom_partie):
    '''pour enregistrer la partie dans le fichier'''
    sauv = open('fichier de sauvegarde', "a")
    nompartie = str(nom_partie)
    sauv.write(nompartie + "\n")
    if mode == 1:
        m = "mode avec un seul joueur"
    if mode == 2:
        m = "mode avec deux joueurs"
    sauv.write(m + "\n")
    code = "le code secret était" + str(code_secret)
    sauv.write(str(code) + "\n")
    if GAGNE is True:
        r = "victoire, le code secret a été deviné"
    if GAGNE is False:
        r = "défaite, le code secret n'a pas été deviné"
    sauv.write(r + "\n")
    nmbre_dessais = "nombred'essais:" + str(current_canva)
    sauv.write(str(nmbre_dessais) + "\n")
    sauv.write(str(tentatives) + "\n")
    sauv.close()
    