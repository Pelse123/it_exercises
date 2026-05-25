"""
**********************************************
nazwa funkcji: NWD
opis funkcji: wyznacza największy wspólny dzielnik liczby a i b
parametry: a - liczba wprowadzona od użytkownika
 b - liczba wprowadzona od użytkownika
zwracany typ i opis: zwracany jest typ int a i jest to wynik NWD
autor: 0000000000000000
***********************************************
"""
def NWD(a,b):
    while a!=b:
        if a>b:
            a = a-b
        else:
            b = b-a
    return a
wartosc_a = int(input())
wartosc_b = int(input())
print(f"NWD {wartosc_a} i {wartosc_b}: {NWD(wartosc_a,wartosc_b)}")