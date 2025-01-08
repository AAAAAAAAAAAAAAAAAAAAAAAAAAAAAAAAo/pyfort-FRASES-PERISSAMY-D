from math import*
from random import*

def factorielle(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def epreuve_math_factorielle():
    n=randint(1,10)
    resultat=factorielle(n)
    print("Calculer la factorielle de ",n)
    reponse=int(input("Votre réponse: "))
    if reponse==resultat :
        return True
    else :
        return False



def est_premier(n):
    premier = True
    for i in range(2,int(sqrt(n))+1):
        if n%i == 0:
            premier = False
    return premier

def premier_plus_proche(n):
    res = 1
    p = True
    while p == True:
        if est_premier(n) == True:
            res = n
            p = False
        n += 1
    return res

def epreuve_math_premier():
    n = randint(10,20)
    print("Epreuve de mathématiques: Trouver le nombre premier le plus proche de ", n)
    rep = int(input("Votre réponse: "))
    if rep == premier_plus_proche(rep):
        return True
    else:
        return False

def epreuve_roulette_mathematique():
    n1 = randint(1, 20)
    n2 = randint(1, 20)
    n3 = randint(1, 20)
    n4 = randint(1, 20)
    n5 = randint(1, 20)
    operation = ["addition", "multiplication", "soustraction"]
    c = choice(operation)
    if c == "addition":
        res = n1 + n2 + n3 + n4 + n5
    elif c == "multiplication":
        res = n1 * n2 * n3 * n4 * n5
    elif c == "soustraction":
        res = n1 - n2 - n3 - n4 - n5
    print("Nombres sur la roulette : [", n1, " " , n2 ," ", n3 ," ", n4 ," " ,n5,"]" )
    print("Calculez le résultat en combinant ces nombres avec une ", c)
    rep = int(input("votre réponse: "))
    if rep == res:
        return True
    else:
        return False

def epreuve_math():
    c = [epreuve_roulette_mathematique, epreuve_math_premier, epreuve_math_factorielle]
    epreuve = choice(c)
    epreuve()








