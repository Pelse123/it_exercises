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

def czy_pierwsza(k):
    if k<2:
        return False
    else:
        i = 2
        while i<(k//2)+1:
            if k%i == 0:
                return False
            i += 1
    return True

def czyLC(k,a):
    if testF(k,a)==1 and czy_pierwsza(k)==False:
        return 1
    else:
        return 0

a = int(input())
while a<2:
    a = int(input())
k = int(input())
while a>k:
    k = int(input())
print(czyLC(k,a))