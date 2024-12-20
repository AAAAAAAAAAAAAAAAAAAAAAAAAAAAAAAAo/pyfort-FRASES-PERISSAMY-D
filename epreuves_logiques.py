def affiche_batonnets(n):
    b = ""
    for i in range(1,n+1):
        b = b + "|"
    print("batonnets restants: ",b)
def joueur_retrait(n):
    j = 0
    while j < 1 or j > 3 and j <= n:
        j = int(input("Combien de batonnet voulez vous retirer?"))
    return j
def maitre_retrait(n):
    if n%4 == 0:
        return 1
    else:
        return n%4
def jeu_nim():
    nb = 20
    tm = False
    while nb != 0:
        if tm == False:
            affiche_batonnets(nb)
            nb = nb - joueur_retrait(nb)
            tm = True
        else:
            print("Le maître du jeu retire ",maitre_retrait(nb), " bâtonnets.")
            nb = nb - maitre_retrait(nb)
            tm = False
    return not tm
jeu_nim()


