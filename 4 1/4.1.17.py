def decymalny_na_binarny(n):
    wynik = ""
    while n != 0:
        wynik = str(n%2) + wynik
        n = n // 2
    return wynik

def decymalny_na_hex(n):
    wynik = ""
    znaki = "0123456789ABCDEF"
    while n != 0:
        reszta = n%16
        wynik = znaki[reszta]+wynik
        n = n // 16
    return wynik

n = int(input())
while n < 0:
    n = int(input())
print(decymalny_na_binarny(n))
print(decymalny_na_hex(n))
