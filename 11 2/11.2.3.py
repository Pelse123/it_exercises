def wyszukiwanie_binarne(tablica,lewo,prawo,n):
    while lewo<=prawo:
        srodek = (lewo+prawo)//2
        if A[srodek]%2 == 0 and A[srodek-1]%2 == 1:
            return srodek
        if A[srodek]%2 == 1:
            return wyszukiwanie_binarne(tablica,srodek+1,prawo,n)
        elif A[srodek]%2 == 0:
            return wyszukiwanie_binarne(tablica,lewo,srodek-1,n)


n = int(input())
while n<0:
    n = int(input())
A=[0]*(n+1)
i = 1
while i<n:
    A[i] = int(input())
    i += 1
A[0]=False
l = 1
p = n-1
w = A[wyszukiwanie_binarne(A,l,p,n)]
print(w)