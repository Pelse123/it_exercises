def pot(a,k):
    i = 0
    wynik = 1
    while i<k:
        wynik = wynik*a
        i += 1
    a = wynik
    return a%k

def testF(k,a):
    i = a
    flaga = True
    while i<k:
        if pot(i,k) != i:
            flaga = False
        i=i+1
    if flaga:
        return 1
    else:
        return 0

a = int(input())
while a<2:
    a = int(input())
k = int(input())
while a>k and k<=2:
    k = int(input())
print(testF(k,a))