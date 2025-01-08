from random import*
def bonneteau():
    L=['A','B','C']
    print("Bienvenue,tu disposes de deux essais pour le trouver À chaque essai, la clé est placée aléatoirement sous l'un des bonneteaux")
    print(L)
    tentatives=2
    a = choice(L)
    for i in range(1,3):
        c=str(input('Choisissez un bonneteau'))
        c=c.upper()
        if c==a :
            return True
        elif c!=a and c in L :
            print("Vous n avez pas trouve la clef")
        else :
            print('Le choix est invalide')
        tentatives=tentatives-1
    print('La cle se trouve sur le bonneteau', a)
    return False


def jeu_lance_des():
    vies = 3
    while vies >= 1:
        t = (randint(1, 6), randint(1, 6))
        print("il vous reste ", vies," vies")
        input("lancer les dés")
        j = (randint(1, 6), randint(1, 6))
        print("vous avez fait ", j[0], " et ", j[1] )
        print(t)
        if j[0] == 6 or j[1] == 6:
            print("v")
            return True
        elif t[0] == 6 or t[1] == 6:
            print("p")
            return False
        else:
            print("personne n'a fait de 6, on passe au lancer suivant")
        vies = vies - 1
    print("aucun des joueurs n'a fait de 6, c'est une égalité")
    return False

def epreuve_hasard():
    c = [jeu_lance_des, bonneteau]
    epreuves = choice(c)
    epreuves()







