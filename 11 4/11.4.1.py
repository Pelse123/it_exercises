def potega_2(k):
    i = 0
    wynik = 1
    while i < k:
        wynik = wynik*2
        i+=1
    return wynik

n = int(input())
lp = 0
i = n
while n != 0:
    while potega_2(i)<=n:
        n = n-potega_2(i)
        lp = lp+1
    else:
        i = i-1
print(lp)



