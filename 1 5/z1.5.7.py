def tworzeniemacierzy(iloscwierszy):
    macierz = []
    for i in range(iloscwierszy):
        wiersz = []
        for j in range(iloscwierszy):
            wiersz.append(int(input()))
        macierz.append(wiersz)
    return macierz

def najwiekszaliczbanaprzekatnej(macierz,iloscwierszy):
    liczba = 0
    for i in range(len(macierz)):
        for j in range(len(macierz[i])):
            if(i==j) or (j+i == iloscwierszy-1):
                if(liczba<macierz[i][j]):
                    liczba = macierz[i][j]
    return liczba


iloscwierszy = int(input())
macierz = tworzeniemacierzy(iloscwierszy)
print(najwiekszaliczbanaprzekatnej(macierz,iloscwierszy))


"""

iloscwierszy = int(input())

def wyswietlaniemacierzy(macierz,iloscwierszy):
    for i in range(len(macierz)):
        for j in range(len(macierz[i])):
            if(i==j) or (j+i == iloscwierszy-1):
                print(f"\033[31m{macierz[i][j]}\033[0m", end=" ")
            else:
                print(f"{macierz[i][j]}", end=" ")

        print()
wyswietlaniemacierzy(macierz, iloscwierszy)

"""

