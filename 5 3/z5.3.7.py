def najdluzszy_podciag_rosnacy(tab):
    maksymalna_dlugosc = 1
    aktualna_dlugosc = 1
    index_podciagu = 0
    for i in range(1,len(tab)):
        if tab[i]>tab[i-1]:
            aktualna_dlugosc +=1
        else:
            if maksymalna_dlugosc<aktualna_dlugosc:
                maksymalna_dlugosc = aktualna_dlugosc
                index_podciagu = i - maksymalna_dlugosc
            aktualna_dlugosc = 1
    if maksymalna_dlugosc < aktualna_dlugosc:
        maksymalna_dlugosc = aktualna_dlugosc
        index_podciagu = len(tab) - maksymalna_dlugosc
    nowa = []
    for i in range(index_podciagu,maksymalna_dlugosc+index_podciagu):
        nowa.append(tab[i])
    return nowa


n = int(input())
tab = []
for i in range(n):
    tab.append(int(input()))
tab = najdluzszy_podciag_rosnacy(tab)
for i in range(len(tab)):
    print(tab[i],end=" ")