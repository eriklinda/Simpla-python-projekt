import random



Start = input("Hej vill du spela ett spel? Ange Ja eller Nej: ")

def spela_spelet():
    # Ställer frågan till spelaren samt sparar ner användarens svar
    svar = int(input("Tänk på ett tal mellan 1-50: "))
    #Här deklareras och genereras det rätta svaret
    ratt_svar = random.randint(1,50)

    #Här kollar programmet ifall svaret är rätt samt ev talar om att det var rätt alt fel
    if svar == ratt_svar:
        print(("Bra jobbat! Ditt svar va {} och det var rätt!").format(svar))
    else:
        print(("Tyvärr du hade fel, ditt svar var {} och rätt svar var {}!").format(svar, ratt_svar))


#Här startas spelet ifall användaren angett Ja eller Nej
if Start == "Ja":
    spela_spelet()
if Start == "Nej":
    print("Vad tråkigt, hoppas du vill spela någon annan gång!")
    quit()
