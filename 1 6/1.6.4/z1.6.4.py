def suma_ASCII(slowo):
    for i in range(1,len(slowo)):
        if ord(slowo[i]) + ord(slowo[i-1]) == 220:
            return slowo
    return False

plik = open("hasla.txt", "r")
zapis = open("wynik4c.txt", "w")

for linia in plik:
    if suma_ASCII(linia.strip()):
        zapis.write(linia)

plik.close()
zapis.close()