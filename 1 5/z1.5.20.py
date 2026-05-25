def utworzmacierz():
    macierz = []
    for i in range (3):
        wiersz = []
        for j in range (3):
            wiersz.append(int(input()))
        macierz.append(wiersz)
    return macierz
def wyznacznik(macierz):
    a = macierz[0][0]
    b = macierz[0][1]
    c = macierz[0][2]
    d = macierz[1][0]
    e = macierz[1][1]
    f = macierz[1][2]
    g = macierz[2][0]
    h = macierz[2][1]
    i = macierz[2][2]
    wyznacznik = a*(e*i-f*h) - b*(d*i-f*g) + c*(d*h-e*g)
    return wyznacznik


print(wyznacznik(utworzmacierz()))


