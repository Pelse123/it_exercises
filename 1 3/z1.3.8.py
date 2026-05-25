ile = int(input())
tablica = []
arytmetyczna = 0
odchylenie = 0


for i in range(ile):
    tablica.append(int(input()))

for i in range(ile):
    arytmetyczna = arytmetyczna + tablica[i]

arytmetyczna = arytmetyczna / ile


for i in range(ile):
    odchylenie = odchylenie +((tablica[i] - arytmetyczna)**2)
odchylenie = (odchylenie/ile)**(1/2)


print(round(odchylenie,2))