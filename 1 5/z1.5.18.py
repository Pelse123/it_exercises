def macierz(iloscwierszy):
    macierz=[]
    for i in range(iloscwierszy):
        wiersz=[]
        for j in range(iloscwierszy):
            if i == j or i+j == iloscwierszy-1:
                wiersz.append(1)
            else:
                wiersz.append(0)

        macierz.append(wiersz)

    for i in range(len(macierz)):
        for j in range(len(macierz[i])):
            print(macierz[i][j], end=" ")
        print()



iloscwierszy = int(input())
macierz(iloscwierszy)



