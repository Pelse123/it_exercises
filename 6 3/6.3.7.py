import statistics
n = int(input())
lista = []
for i in range(n):
    lista.append(float(input()))

print("Średnia:",round(statistics.mean(lista),2))
print("Mediana:",round(statistics.median(lista),2))
print("Moda:",round(statistics.mode(lista),2))