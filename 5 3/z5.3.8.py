def maksymalna_suma_podciagu(ciag):
    aktualna_suma = 0
    max_suma = -1000000
    index_poczatkowy = 0
    temp_index = 0
    index_ostatni = 0
    for i in range(len(ciag)):
        aktualna_suma += ciag[i]
        if max_suma < aktualna_suma:
            max_suma = aktualna_suma
            index_ostatni = i
            index_poczatkowy = temp_index
        if aktualna_suma < 0:
            aktualna_suma = 0
            temp_index = i+1
    for i in range(index_poczatkowy,index_ostatni+1):
        print(ciag[i],end=" ")
n = int(input())
tab = []
for i in range(n):
    tab.append(int(input()))
maksymalna_suma_podciagu(tab)