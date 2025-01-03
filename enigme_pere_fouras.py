import json
from random import*
def charger_enigmes(fichier):
    with open(fichier,"r",encoding='utf-8') as f:
        contenu = json.load(f)
    enigme = [None]*len(contenu)
    for i in range(len(contenu)):
        enigme[i] = {"question" : contenu[i]["question"],"reponse": contenu[i]["reponse"]}
    return enigme

def enigme_pere_fouras():
    e = charger_enigmes(r"C:\Users\benja\PycharmProjects\pyfort-FRASES-PERISSAMY-D\enigmesPF.json")
    question = choice(e)
    q = question["question"]
    nb_essais = 3
    print(q)
    while nb_essais != 0:
        r = input("Quelle est votre réponse ? : ")
        r = r.lower()
        if r == question["reponse"].lower():
            print("Vous avez trouvé la bonne réponse")
            return True
        else:
            nb_essais = nb_essais - 1
            print("Mauvaise réponse, il vous reste ", nb_essais, " essais")
    print("Vous avez échoué, la bonne réponse était : ", question["reponse"])
    return False
