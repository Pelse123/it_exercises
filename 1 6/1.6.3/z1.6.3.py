def czy_palindrom(slowo):
    for i in range(len(slowo)//2):
        if slowo[i] != slowo[len(slowo)-1-i]:
            return False
    return True

plik = open("hasla.txt", "r")
zapis = open("wynik4b.txt", "w")

for linia in plik:
    if czy_palindrom(linia.strip()):
        zapis.write(linia)

plik.close()
zapis.close()