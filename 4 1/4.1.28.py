def dodaj_zera(l,ilezer):
    wynik = l
    for i in range(ilezer):
        wynik = "0"+ wynik
    return wynik

def dodaj_zera_mnozenie(l,ilezer):
    wynik = l
    for i in range(ilezer):
        wynik = wynik + "0"
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

def mnozenie_binarne(l1,l2):
    suma = "0"
    for i in range(len(l2)-1,-1,-1):
        wynik_mnozenia_cyfr = ""
        for j in range(len(l1)-1,-1,-1):
            iloczyn = int(l2[i])*int(l1[j])
            wynik_mnozenia_cyfr = str(iloczyn) + wynik_mnozenia_cyfr
        wynik_mnozenia_cyfr = dodaj_zera_mnozenie(wynik_mnozenia_cyfr,len(l2)-1-i)
        suma = dodawanie_binarne(suma,wynik_mnozenia_cyfr)
    return suma


l1,l2 = input(),input()
print(mnozenie_binarne(l1,l2))
