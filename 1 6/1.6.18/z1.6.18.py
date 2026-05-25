def czy_palindrom(slowo):
    for i in range(len(slowo)//2):
        if slowo[i] != slowo[len(slowo)-1-i]:
            return False
    return True

plik = open("liczby.txt", "r")
zapis = open("wynik5.txt", "w")
zapis.write("b)\n")
for line in plik:
    if czy_palindrom(line.strip()):
        zapis.write(line)
plik.close()
zapis.close()