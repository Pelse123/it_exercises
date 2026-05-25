def utworzmacierz(iloscwierszy,ilosckolumn):
    macierz = []
    for i in range(iloscwierszy):
        wiersz = []
        for j in range(ilosckolumn):
            wiersz.append(input())
        macierz.append(wiersz)
    return macierz

def zamiana(literka):
    if(literka >= "A" and literka <= "Z"):
        literka = ord(literka) + 32
        return chr(literka)
    else:
        return literka

def macierzmalychliterek(macierz):
    for i in range(len(macierz)):
        for j in range(len(macierz[i])):
            print(zamiana(macierz[i][j]),end=" ")
        print()



iloscwierszy = int(input())
ilosckolumn = int(input())
macierz = utworzmacierz(iloscwierszy,ilosckolumn)
macierzmalychliterek(macierz)