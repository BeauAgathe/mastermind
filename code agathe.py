'''agathe'''


def sauvegarder(nom_partie):
    '''pour enregistrer la partie dans le fichier'''
    sauv = open('fichier de sauvegarde', "w")
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
