
def czy_palindrom(slowo):
    for i in range(len(slowo)//2):
        if slowo[i] != slowo[len(slowo)-1-i]:
            return False
    return True

plik = open("dane.txt", "r")
zapis = open("zadanie4.txt", "w")

for linia in plik:
    if czy_palindrom(linia.strip()):
        zapis.write(linia)

plik.close()
zapis.close()