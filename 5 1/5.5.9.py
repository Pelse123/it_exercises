def policz_wielomian_rekurencyjnie(stopien, liczby, x):
    if stopien == 0:
        return liczby[0]
    return x * policz_wielomian_rekurencyjnie(stopien - 1, liczby, x) + liczby[stopien]


stopien = int(input())
liczby = []
for i in range(stopien + 1):
    n = int(input())
    liczby.append(n)
x = int(input())

print(policz_wielomian_rekurencyjnie(stopien, liczby, x))
