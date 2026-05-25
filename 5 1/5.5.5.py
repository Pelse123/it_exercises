def wykonaj_potegowanie_szybkie_iteracyjnie(a,b):
    wynik = 1
    while b>0:
        if b%2!=0:
            wynik = wynik*a
        a = a*a
        b = b//2
    return wynik

a = int(input())
b = int(input())
print(wykonaj_potegowanie_szybkie_iteracyjnie(a,b))
