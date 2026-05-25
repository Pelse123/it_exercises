def tworzeniemacierzy(iloscwierszy,ilosckolumn):
    macierz = []
    for i in range(iloscwierszy):
        wiersz = []
        for j in range(ilosckolumn):
            wiersz.append(int(input()))
        macierz.append(wiersz)
    return macierz

def suma(macierz):
    sumaparzystych = 0
    sumanieparzystych = 0
    for i in range(len(macierz)):
        for j in range(len(macierz[i])):
            if macierz[i][j]%2==0:
                sumaparzystych += macierz[i][j]
            else:
                sumanieparzystych += macierz[i][j]
    print(sumaparzystych)
    print(sumanieparzystych)



iloscwierszy = int(input())
ilosckolumn = int(input())
macierz = tworzeniemacierzy(iloscwierszy,ilosckolumn)
suma(macierz)