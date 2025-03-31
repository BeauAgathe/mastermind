'''agathe'''


def sauvegarder():
    '''pour enregistrer la partie dans le fichier'''
    sauv = open('fichier de sauvegarde', "w")
    sauv.close()


def voir_vieilles_parties():
    '''pour regarder les infos des parties enregistrées'''
    fichier = open('fichier de sauvegarde', "r")
    fichier.close()
