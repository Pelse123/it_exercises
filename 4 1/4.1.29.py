def dodaj_zera(l,ilezer):
    wynik = l
    for i in range(0,ilezer):
        wynik = "0"+wynik
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

system = int(input())
l1,l2 = input(),input()
print(dodawanie_system(l1,l2,system))
