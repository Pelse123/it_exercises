def policzSrednia(lista):
    return sum(b for a, b in lista)/len(lista)
lista_studentow = [("Jan", 4.5), ("Anna", 5.0), ("Piotr", 3.5)]

print(policzSrednia(lista_studentow))
