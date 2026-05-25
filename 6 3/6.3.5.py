osoba1 = [10, 8, 9, 7, 10]
osoba2 = [9, 9, 8, 8, 7]
osoba3 = [8, 10, 7, 9, 9]
lista = list(zip(osoba1, osoba2, osoba3))
for i in range(len(lista)):
    for j in range(len(lista[i])):
        osoba = 0
        if lista[i][j] == max(lista[i]):
            osoba = j
    print(f"Konkurencja {i+1}: Najwyższy wynik {max(lista[i])} zdobyła Osoba {osoba+1}")
