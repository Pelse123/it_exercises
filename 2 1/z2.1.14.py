def pierwsza_literka(slowo):
    return slowo[0]

slownik = {}
ilosc = int(input())

for i in range(ilosc):
    wartosc = input()
    klucz =  pierwsza_literka(wartosc)

    if klucz in slownik:
        slownik[klucz].append(wartosc)
    else:
        slownik[klucz] = [wartosc]

print(slownik)