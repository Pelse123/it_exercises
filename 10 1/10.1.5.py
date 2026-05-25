macierz = []
d = int(input())
tekst = input()
s = 0
szyfr =""
wielkosc_macierzy = 0
for i in range(1,d):
    if(i**2)>d:
        wielkosc_macierzy = i
        break
iterator_po_napisie = 0
for i in range(wielkosc_macierzy):
    wiersz = []
    for j in range(wielkosc_macierzy):
        if iterator_po_napisie<d:
            if tekst[iterator_po_napisie]==" ":
                wiersz.append("_")
            else:
                wiersz.append(tekst[iterator_po_napisie])
            iterator_po_napisie += 1
        else:
            wiersz.append("_")
    macierz.append(wiersz)
for i in range(len(macierz[0])):
    for j in range(len(macierz)):
        szyfr = szyfr+macierz[j][i]
s = len(szyfr)
print(s)
print(szyfr)


