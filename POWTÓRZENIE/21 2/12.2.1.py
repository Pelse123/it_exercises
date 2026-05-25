def napraw_slownik(slownik):
    slownik_bez_0 = {}
    for klucz in slownik:
        wartosc = slownik[klucz]
        if wartosc != 0:
            slownik_bez_0[klucz] = wartosc

    slownik = slownik_bez_0.copy()

    srednia = 0
    for klucz in slownik:
        wartosc = slownik[klucz]
        srednia += wartosc

    srednia /= len(slownik)

    wynik_slownik = {}
    for klucz in slownik:
        wartosc = slownik[klucz]
        if wartosc >= srednia:
            wynik_slownik[klucz] = wartosc
    return wynik_slownik


liczba_kluczy = int(input())
slownik = {}
for i in range(liczba_kluczy):
    klucz = input()
    wartosc = int(input())
    slownik[klucz.replace(" ","")] = wartosc

wynik_slownik = napraw_slownik(slownik)
for klucz in wynik_slownik:
    wartosc = wynik_slownik[klucz]
    print(wartosc, "->", klucz)



