def czy_same_literki(liczba):
    for i in range(len(liczba)):
        if ord(liczba[i]) < 65 or ord(liczba[i])>75:
            return False
    return True
plik = open("liczby_hex.txt","r")
zapis = open("wyniki_hex.txt","w")
licznik = 0
zapis.write("c)\n")
for linia in plik:
    cyfra = linia.strip()
    if czy_same_literki(cyfra):
        zapis.write(cyfra+"\n")

zapis.close()
plik.close()