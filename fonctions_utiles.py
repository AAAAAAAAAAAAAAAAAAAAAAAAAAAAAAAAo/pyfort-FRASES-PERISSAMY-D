import json
from random import*
def salle_De_Tresor():
    with open(r"C:\Users\benja\PycharmProjects\pyfort-FRASES-PERISSAMY-D\indicesSalle.json","r",encoding='utf-8') as f:
        jeu_tv = json.load(f)
    a = choice(list(jeu_tv["Fort Boyard"].keys()))
    annee = jeu_tv["Fort Boyard"][a]
    e = choice(list(annee.keys()))
    emission = jeu_tv["Fort Boyard"][a][e]
    indices = emission["Indices"]
    mot_code = emission["MOT-CODE"]
    print(indices[:3])
    essais = 3
    reponse_correcte = False
    while essais > 0 and reponse_correcte == False:
        r = input("Quelle est votre réponse ? : ")
        r = r.upper()
        if r == mot_code:
            reponse_correcte = True
        else:
            essais = essais - 1
            print("il vous reste ", essais," essais")
            print(indices[5 - essais])
    print("Le mot de passe était : ", mot_code)
    if reponse_correcte == True:
        print("Bravo vous avez gagné !")
    else:
        print("Vous avez perdu")
