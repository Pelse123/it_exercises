n = int(input())
lista = []
for i in range(n):
    lista.append(int(input()))
lista.insert(0,0)
lista.append(101)
print(lista)
lista.sort(reverse=True)
print(lista)
print("Największy element listy: ",max(lista))
print("Najmniejszy element listy: ",min(lista))
