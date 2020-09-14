import requests
import json

#Länk att hämta json data ifrån!
endpoint = 'http://dummy.restapiexample.com/api/v1/employees'

#Gör en session
r = requests.session()

#Skickar förfrågan till sidan att hämta data
s = r.get(url=endpoint)

#Sparar ner responsen och gör om det till python objekt
data = json.loads(s.text)

#Printar ut responsen!
#print(data["data"])


#Gör listor för varje kategori!
anstlldas_namn = []
anstlldas_aldrar = []

#Printar ut bara de anställdas namn!
for anstalld in data["data"]:
    #Sparar ner namnen i listan som är skapad
    anstlldas_namn.append(anstalld['employee_name'])



#Printar ut alla deras åldrar
for alder in data["data"]:
    #aldrar = alder['employee_age']

    #Sparar ner allas åldrar till listan som är skapad
    anstlldas_aldrar.append(alder['employee_age'])


#Printar ut listorna med namn och ålder
print("De är såhär gamla: " + str(anstlldas_aldrar))
print("De heter även såhär: " + str(anstlldas_namn))
