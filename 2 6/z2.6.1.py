def sortujKrotki(lista):
    return sorted(lista,key=lambda x:(x[0],x[1]))
ilosc_krotek = int(input())
lista = []
for i in range(ilosc_krotek):
    lista.append((input(),int(input())))


print(sortujKrotki(lista))