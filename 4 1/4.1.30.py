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

def zamiana_liter_na_liczby(znak):
    if ord(znak) >= 65 and ord(znak) <= 90:
        return ord(znak)-55
    return int(znak)

def zamiana_liczb_na_znak(literka):
    if literka>9:
        return(chr(literka+55))
    return str(literka)

def dodawanie_system(l1,l2,system):
    wynik = ""
    if len(l1) > len(l2):
        l2=dodaj_zera(l2,len(l1)-len(l2))
    if len(l1) < len(l2):
        l1=dodaj_zera(l1,len(l2)-len(l1))
    przeniesienie = 0
    for i in range(len(l1)-1,-1,-1):
        suma = przeniesienie
        suma = suma + zamiana_liter_na_liczby(l1[i])
        suma = suma +zamiana_liter_na_liczby(l2[i])
        if suma>=system:
            przeniesienie = 1
            suma = suma-system
        else:
            przeniesienie = 0
        wynik = zamiana_liczb_na_znak(suma) + wynik
        if i==0 and przeniesienie>0:
            wynik = zamiana_liczb_na_znak(przeniesienie)+wynik
    return wynik

def mnozenie_system(system,l1,l2):
    suma = "0"
    for i in range(len(l2)-1,-1,-1):
        wynik_mnozenia_cyfr = ""
        przeniesienie = 0
        for j in range(len(l1)-1,-1,-1):
            iloczyn = zamiana_liter_na_liczby(l2[i])*zamiana_liter_na_liczby(l1[j])+przeniesienie

            if iloczyn>=system:
                przeniesienie = iloczyn//system
                iloczyn = iloczyn%system
            else:
                przeniesienie = 0

            wynik_mnozenia_cyfr = zamiana_liczb_na_znak(iloczyn) + wynik_mnozenia_cyfr
            if j == 0 and przeniesienie>0:
                wynik_mnozenia_cyfr = zamiana_liczb_na_znak(przeniesienie) + wynik_mnozenia_cyfr

        wynik_mnozenia_cyfr = dodaj_zera_mnozenie(wynik_mnozenia_cyfr,len(l2)-1-i)
        suma = dodawanie_system(suma,wynik_mnozenia_cyfr,system)
    return suma


system,l1,l2 = int(input()),input(),input()
print(mnozenie_system(system,l1,l2))
