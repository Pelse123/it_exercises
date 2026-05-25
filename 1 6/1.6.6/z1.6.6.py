def suma_cyfr(slowo):
    suma = 0
    for i in range(len(slowo)):
        suma += int(slowo[i])
    return suma
plik = open("cyfry.txt", "r")
zapis = open("zadanie4.txt", "w")

maks = 0
mini = int(plik.readline().strip())
liczbamaks = 0
liczbamin = 0

for linia in plik:
    if suma_cyfr(linia.strip()) > maks:
        maks = suma_cyfr(linia.strip())
        liczbamaks = linia.strip()
    if suma_cyfr(linia.strip()) < mini:
        mini = suma_cyfr(linia.strip())
        liczbamin = linia.strip()

zapis.write(f"b)\nLiczba z najwieksza suma cyfr: {liczbamaks}\nLiczba z najmniejsza suma cyfr: {liczbamin}\n")

plik.close()
zapis.close()
