def na_binarny(l):
    wynik = 0
    while l>0:
        if l%2==1:
            wynik+=1
        l=l//2
    return wynik

L = int(input())
w = 0
while L>0:
    ostatnia_liczba = L%10
    w += na_binarny(ostatnia_liczba)
    L = L//10
print(w)
