import random


antal = int(input("Hur många gånger skall tärningen slås?"))


def Dice(antal):
    #dice = random.randrange(1,6)
    slag = 0
    resultat = []

    while antal > slag:
        slag += 1
        dice = random.randrange(1, 6)
        print(("Kast nr{} blev {}!").format(slag, dice))
        resultat.append(dice)

Dice(antal)
