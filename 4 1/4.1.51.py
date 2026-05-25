def licz_miejsca(n):
    licznik = 0
    while n>0:
        licznik = licznik + 1
        n = n >> 1
    return licznik

n = int(input())
ilosc = licz_miejsca(n)
temp = n
flaga = "TAK"
for i in range(ilosc):
    if n&1 != ((temp>>ilosc-1)&1):
        flaga = "NIE"
        break
    n = n >> 1
    temp = temp<< 1
print(flaga)

