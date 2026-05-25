def filtrujDane(lista):
    return list(map(lambda x: x**2,filter(lambda x: x if x>0 else False,lista)))

n = int(input())
lista = [int(input()) for i in range(n)]
lista = filtrujDane(lista)
for i in range(len(lista)):
    print(lista[i],end=" ")
