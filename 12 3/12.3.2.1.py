def pot(a,k):
    i = 0
    wynik = 1
    while i<k:
        wynik = wynik*a
        i += 1
    a = wynik
    return a%k

a = int(input())
while a<2:
    a = int(input())
k = int(input())
while a>k:
    k = int(input())
print(pot(a,k))