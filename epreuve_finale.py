def introduction():
    print('Bienvenue dans le jeu')
    print('Vous devez accomplir des épreuves pour gagner des clés afin de déverrouiller la salle du trésor')
    print("L'objectif est de ramasser trois clés pour accéder à la salle du trésor")
    print('Vous avez le choix entre les épreuves de hasard, les épreuves logiques et les épreuves mathématiques.')



def composer_equipe():
    equipe = []
    nb = 4
    l = False
    while nb <= 0 or nb > 3 :
        nb = int(input("Combien de joueurs y a t il dans votre équipe ? "))
    equipe = [None] * nb
    for i in range(nb):
         equipe[i] = {"nom" : "", "profession" : "" , "role": "", "cles_gagnées": 0}
         equipe[i]["nom"] = str(input("rentrez votre nom : "))
         equipe[i]["profession"] = str(input("rentrez votre profession : "))
         if l == False:
            equipe[i]["role"] = str(input("etes vous le leader ? leader/membre : "))
            if equipe[i]["role"] == "leader":
                l = True
         elif l == True:
             equipe[i]["role"] = "membre"
    if l == False:
        n_l = str(input("veuillez entrer le nom du leader : "))
        n = 0
        while n_l != equipe[n]["nom"]:
            n = n+1
            if n_l == equipe[n]["nom"]:
                equipe[n]["role"] = "leader"
    return equipe



def menu_epreuves():
    print('Choississez le numero de l epreuve')
    print('1. Épreuve de Mathématiques')
    print('2. Épreuve de Logique')
    print('3. Épreuve du hasard')
    print('4. Énigme du Père Fouras')
    n=input("Saisir le numero de l'epreuve : ")
    return(n)

def choisir_joueur(equipe):
    for i in range(len(equipe)):
        print(i+1, ". ", equipe[i]["nom"]," (", equipe[i]["profession"], ") - ", equipe[i]["role"])
    a=int(input('Entrez le numero du joueur souhaité : '))
    return(equipe[a-1])
