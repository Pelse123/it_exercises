
pesel = input()
tablicamnozenia = [1,3,7,9,1,3,7,9,1,3,1]
suma = 0
licznik = 0
for i in range(len(pesel)):
    liczba = ord(pesel[i])-48
    suma = suma+(liczba*tablicamnozenia[i])
    licznik = licznik+1

if(suma%10==0) and (licznik==11):
    print("Podany PESEL jest poprawny")
else:
    print("Podany PESEL jest niepoprawny")