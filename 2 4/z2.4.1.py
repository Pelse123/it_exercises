def usun_powtorzenia(tablica):
    return set(tablica)

napis = input()
czy_izogram = usun_powtorzenia(napis)

if len(czy_izogram)<len(napis):
    print("NIE")
else:
    print("TAK")