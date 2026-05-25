def polacz_tablice(tablica1, tablica2):
    wspolna_tablica = []
    for i in range (len(tablica1)):
        wspolna_tablica.append(tablica1[i])
    for i in range (len(tablica2)):
        wspolna_tablica.append(tablica2[i])
    return wspolna_tablica
def polacz_tablice2(tablica1, tablica2):
    return tablica1+tablica2

n1 = int(input())
tabn1 = []
for i in range(n1):
    tabn1.append(int(input()))

n2 = int(input())
tabn2 = []
for i in range(n2):
    tabn2.append(int(input()))

print(polacz_tablice(tabn1, tabn2))
print(polacz_tablice2(tabn1, tabn2))
print(tabn1+tabn2)
