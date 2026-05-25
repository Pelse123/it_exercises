def szyfr_kolumnowy(slowo,klucz):
    macierz = []
    k = 0
    for i in range(klucz):
        wiersz=[]
        for j in range(klucz):
            if k<len(slowo):
                wiersz.append(slowo[k])
                k=k+1
            else:
                wiersz.append("X")
        macierz.append(wiersz)
    szyfrogram = ""
    for i in range(klucz):
        for j in range(klucz):
            szyfrogram+=macierz[j][i]
    return szyfrogram

def minimalna_macierz(slowo):
    mini_wielkosc= 0
    i = 0
    while True:
        if i*i>=len(slowo):
            mini_wielkosc=i
            break
        i+=1
    return mini_wielkosc

pierwszy_napis =input()
drugi_napis = input()
if szyfr_kolumnowy(drugi_napis,minimalna_macierz(pierwszy_napis))==pierwszy_napis:
    print("TAK")
else:
    print("NIE")


