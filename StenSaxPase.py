import random

#Gör en lista som innehåller de tre alternativen
val = ["Sten", "Sax", "Påse"]

#Gör en funktion åt datorns tur så de kan spelas flera gånger utan att bli samma resultat
def Datorns_drag():
    drag = random.choice(val)
    return drag

#Startar med att printa ut alternativen
Start = input("Sten, Sax eller påse?")

def Match(spelare, dator):

    if spelare==dator:
        return "Oavgjort!"
    elif spelare==val[0] and dator==val[1] or spelare==val[1] and dator==val[2] or spelare==val[2] and dator==val[0]:
        return "Du vann!"
    elif spelare==val[1] and dator==val[0] or spelare==val[2] and dator==val[1] or spelare==val[0] and dator==val[2]:
        return "Du förlorade!"

print(Match(Start,Datorns_drag()))