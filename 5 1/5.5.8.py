def policz_wielomian_iteracyjnie(liczby,x):
    wynik=liczby[0]
    for i in range(1,len(liczby)):
        wynik = x * wynik + liczby[i]
    return wynik

stopien = int(input())
liczby = []
for i in range(stopien+1):
    n = int(input())
    liczby.append(n)
x = int(input())
print(policz_wielomian_iteracyjnie(liczby,x))