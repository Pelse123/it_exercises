def dodaj_zera(l,ilezer):
    wynik = l
    for i in range(0,ilezer):
        wynik = "0"+wynik
    return wynik

def dodawanie_binarne(l1,l2):
    wynik = ""
    if len(l1) > len(l2):
        l2=dodaj_zera(l2,len(l1)-len(l2))
    if len(l1) < len(l2):
        l1=dodaj_zera(l1,len(l2)-len(l1))
    przeniesienie = 0
    for i in range(len(l1)-1,-1,-1):
        suma = przeniesienie
        suma = suma + int(l1[i])
        suma = suma +int(l2[i])
        if suma>=2:
            przeniesienie = 1
            suma = suma-2
        else:
            przeniesienie = 0
        wynik = str(suma) + wynik
        if i==0 and przeniesienie>0:
            wynik = str(przeniesienie)+wynik
    return wynik

l1,l2 = input(),input()
print(dodawanie_binarne(l1,l2))
