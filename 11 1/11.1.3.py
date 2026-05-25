def Najwiekszy_Czynnik(n):
    wynik = 0
    i = 2
    while n > 1:
        if n % i == 0:
            if wynik<i:
                wynik = i
            n = n / i
        else:
            i = i + 1
    return wynik

n = int(input())
d = Najwiekszy_Czynnik(n)
print(d)
