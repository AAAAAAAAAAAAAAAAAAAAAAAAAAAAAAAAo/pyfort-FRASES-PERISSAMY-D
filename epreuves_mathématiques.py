from math import*
from random import*
def est_factorielle(n):
    print(" ")






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
        n += n
    return res

def epreuve_math_premier():
    n = randint(10,20)
    rep = int(input("Epreuve de mathématiques: Trouver le nombre premier le plus proche de ",n,"."))
    print("Votre réponse: ",rep)
    if rep == premier_plus_proche():
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
    rep = int(input("Calculez le résultat en combinant ces nombres avec une ," + c))
    print("votre réponse: ", rep)
    if rep == res:
        return True
    else:
        return False

def epreuve_math():
    c = [epreuve_roulette_mathematique, epreuve_math_premier, est_factorielle]
    epreuve = choice(c)








