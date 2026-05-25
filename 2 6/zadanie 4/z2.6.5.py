def usun_podany(x,wynik):
    if x in wynik:
        wynik.remove(x)


plik = open("instrukcje.txt", "r")
zapis = open("wyniki.txt", "w")

wynik = []

slownik = {
    "STABILIZE":lambda y : list(filter(lambda x : usun_podany(x,wynik) if x<0 else False, wynik)),
    "DISCHARGE":lambda x :usun_podany(x,wynik),
    "CHARGE":lambda x : wynik.append(x)
}

for linia in plik:
    wiersz = linia.strip().split(sep=" ")
    funkcja = wiersz[0]
    liczba = int(wiersz[1])
    slownik[funkcja](liczba)

for i in wynik:
    zapis.write(f"{i} ")
plik.close()
zapis.close()