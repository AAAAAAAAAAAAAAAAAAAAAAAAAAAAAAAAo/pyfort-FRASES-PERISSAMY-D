from epreuves_mathématiques import *
from epreuves_hasard import *
from epreuves_logiques import*
from epreuve_finale import*

def jeu():
    introduction()
    e = composer_equipe()
    nb_cle = 0
    while nb_cle != 3:
        choix_epreuve = menu_epreuves()
        choix_joueur = choisir_joueur(e)
        if choix_epreuve == 1:
            epreuve = epreuve_math()
            if epreuve == True:
                print("vous avez gagné une clé")
                choix_joueur["cles_gagnées"] += 1
                nb_cle += 1
        elif choix_epreuve == 2:
            epreuve = jeu_nim
            if epreuve == True:
                print('Vous avez gagne')
                choix_joueur["cles_gagnées"] += 1
                nb_cle += 1
        elif choix_epreuve == 3:
            epreuve = epreuve_hasard()
            if epreuve == True:
                print("vous avez gagné une clé")
                choix_joueur["cles_gagnées"] += 1
                nb_cle += 1
        #elif choix_epreuve == 4:
            #epreuve = enigme_pere_fouras()
            #if epreuve == True:
                #print("vous avez gagné une clé")
                #choix_joueur["cles_gagnées"] += 1
                #nb_cle += 1







