def push(stos,wartosc):
    stos.append(wartosc)
    return stos

def pop(stos):
    return stos.pop()

def isEmpty(stos):
    return len(stos)==0

def first(stos):
    return stos[-1]

def wczytaj_stos_po_znakach(dane):
    stos = []
    for i in dane:
        push(stos,i)
    return stos
def wczytaj_stos_po_slowach(dane):
    slowa = dane.split()
    stos = []
    for i in slowa:
        push(stos,i)
        push(stos," ")
    stos.pop()
    return stos

def odczytaj_stos(stos):
    while isEmpty(stos)==False:
        print(first(stos),end="")
        pop(stos)

dane = input()
po_znakach_stos = wczytaj_stos_po_znakach(dane)
po_slowach_stos = wczytaj_stos_po_slowach(dane)
odczytaj_stos(po_znakach_stos)
print()
odczytaj_stos(po_slowach_stos)
