def creer_sapin(taille):
    for x in range(taille):
        for spaces in range(taille - (x + 1)):
            print(" ", end='')
        for chevrons in range((x + 1)* 2):
            print("^", end='')
        print("\n")
creer_sapin(5)

