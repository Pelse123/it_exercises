def suma_rekurencyjnie(tablica_kluczy,i=0):
    if i == len(tablica_kluczy):
        return 0
    else:
        return tablica_kluczy[i] + suma_rekurencyjnie(tablica_kluczy,i+1)

slownik = {}
n = int(input())

for i in range(n):
    klucz = input()
    wartosc = int(input())
    slownik[klucz] = wartosc

tablica_kluczy = []
for klucz in slownik:
    tablica_kluczy.append(slownik[klucz])

print(suma_rekurencyjnie(tablica_kluczy))
