def push(stos,n):
    return stos.append(n)

def pop(stos):
    return stos.pop()

def peek(stos):
    return stos[len(stos)-1]

def isEmpty(stos):
    return len(stos)==0

ilosc = int(input())
stos = []

for i in range(ilosc):
    liczba = int(input())
    push(stos,liczba)

maks = -1
ostatnia = peek(stos)
tablica_elementow = []
tablica_wartosci_po_prawej = []

while not isEmpty(stos):
    if(peek(stos)<ostatnia):
        maks = ostatnia
    tablica_elementow.append(peek(stos))
    tablica_wartosci_po_prawej.append(maks)
    ostatnia = peek(stos)
    pop(stos)


for i in range(ilosc):
    print(f"{tablica_elementow[len(tablica_elementow)-1-i]}: {tablica_wartosci_po_prawej[len(tablica_elementow)-1-i]} ")
