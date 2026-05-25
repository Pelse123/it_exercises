def F_iteracyjnie(i,n,a):
    wynik = i
    for j in range(i,n):
        if a[wynik]>a[j]:
            wynik = j
    return wynik

n = int(input())+1
a = [0]*n
a[0] = False
for i in range(1,n):
    a[i] = int(input())
print(F_iteracyjnie(9,n,a))

