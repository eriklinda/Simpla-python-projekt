

def miniraknare():
    # Frågar användaren efter tal 1
    tal1 = int(input("Ange ett tal: "))
    # Frågar efter tal nr 2
    tal2 = int(input("Ange ett till tal: "))
    #Frågar vilken metod som skall användas
    metod = input("Vad vill du göra med dessa tal? (*, +, -, /) ")

    #Använder det korrekt angivna räknesättet samt printar ut rätt svar
    if metod == "+":
        svar = tal1 + tal2
        print(("Summan av dina tal är: %s!") % svar)
    if metod == "-":
        svar = tal1 - tal2
        print(("Differensen på dina tal är: %s!") % svar)
    if metod == "/":
        svar = tal1 / tal2
        print(("Kvoten på dina tal är: {}!").format(svar))
    if metod == "*":
        svar = tal1 * tal2
        print("Produkten av dina tal är: " + svar + "!")

    #kalkylator = tal1 + metod + tal2
    #print(kalkylator)
miniraknare()
