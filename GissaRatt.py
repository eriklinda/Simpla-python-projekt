import random



Start = input("Hej vill du spela ett spel? Ange Ja eller Nej: ")

def spela_spelet():
    # Ställer frågan till spelaren samt sparar ner användarens svar
    svar = int(input("Tänk på ett tal mellan 1-50: "))
    ratt_svar = random.randint(1,50)
    if svar == ratt_svar:
        print(("Bra jobbat! Ditt svar va {} och det var rätt!").format(svar))
    else:
        print(("Tyvärr du hade fel, ditt svar var {} och rätt svar var {}!").format(svar, ratt_svar))



if Start == "Ja":
    spela_spelet()
if Start == "Nej":
    print("Vad tråkigt, hoppas du vill spela någon annan gång!")
    quit()
