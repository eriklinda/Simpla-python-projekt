
#Frågar användaren efter ett ord att kolla i
i = input("Ange vilket ord  vill du räkna ut antal vokaler i? ")


#Gör funktionen för att deklarera alla vokaler samt göra en lista där alla vokaler skall läggas in i
def rakna_vokaler(ordet):
    #Deklarerar alla vokaler i en lista
    vokaler = ["a", "e", "i", "o", "u", "y", "å", "ä", "ä"]
    #Gör en lista där alla vokaler i order skall läggas till i
    antal_vokaler = []

    #Löper igenom alla bokstäver i order samt kollar ifall det finns någon vokal
    #Väljer att göra alla bokstäver till små för att vokalerna är deklarerade i småbokstäver
    for vokal in ordet.lower():
        #Kollar ifall det finns någon vokal
        if vokal in vokaler:
            #Lägger till alla vokaler i listan som är skapad
            antal_vokaler.append(vokal)
        else:
            return print("Det finns ingen vokal i ditt ord")

    #Räknar alla ev vokaler och lämnar tillbaka dem
    return len(antal_vokaler)
#Printar ut resultatet
print(("Det är {}st vokaler i ordet {}!").format(rakna_vokaler(i), i))