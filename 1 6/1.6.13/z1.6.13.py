def odbicie_lustrzane(slowo):
    odbicie = ""
    for i in range(len(slowo)):
        odbicie = odbicie + slowo[len(slowo) - i - 1]
    return odbicie


plik2 = open("slowa.txt", "r")
plik = open("nowe.txt", "r")
zapis = open("wynik5.txt", "w")
tablica_slow = []

for linia in plik:
    tablica_slow.append(linia.strip())

tablica_wystapien = [0] * len(tablica_slow)
tablica_lustrzanych_wystapien = [0] * len(tablica_slow)
aktualne_slowo = ""

for linia in plik2:
    aktualne_slowo = linia.strip()
    for i in range(len(tablica_slow)):
        if tablica_slow[i] == aktualne_slowo:
            tablica_wystapien[i] = tablica_wystapien[i]+1
        if tablica_slow[i] == odbicie_lustrzane(aktualne_slowo):
            tablica_lustrzanych_wystapien[i] = tablica_lustrzanych_wystapien[i]+1

zapis.write("b)\n")
for i in range(len(tablica_wystapien)):
    zapis.write(f"{tablica_slow[i]} {tablica_wystapien[i]} {tablica_lustrzanych_wystapien[i]}\n")

plik2.close()
plik.close()
zapis.close()
