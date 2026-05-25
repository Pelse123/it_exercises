def czy_palindrom(slowo):
    for i in range(len(slowo)//2):
        if(slowo[i] != slowo[len(slowo)-1-i]):
            return False
    return True
zmienna = 4**(1/2)
print(round(zmienna))
ilosc = int(input())
slownik={}

for i in range(ilosc):
    klucz = input()
    wartosc = input()
    slowo_klucz_i_wartosc = klucz+wartosc
    if(czy_palindrom(slowo_klucz_i_wartosc)):
        slownik[klucz] = wartosc

for klucz in slownik:
    print(f"{klucz}: {slownik[klucz]}")

