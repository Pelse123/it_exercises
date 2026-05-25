
def licz_bity(n):
    licznik = 0
    while n>0:
        if n&1 == 1:
            licznik = licznik + 1
        n = n >> 1
    return licznik


n = int(input())
print(licz_bity(n))
