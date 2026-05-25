def zadanie1_1(tablica,n):
    lewo = 1
    prawo = n
    while lewo<=prawo:
        srodek = (lewo+prawo)//2
        if tablica[srodek]%2==0 and tablica[srodek-1]%2!=0:
            return srodek
        if tablica[srodek]%2!=0:
            lewo = srodek+1
        else:
            prawo = srodek-1
    return -1

#test do zadania 1_1
n = 10
A = [False,5,99,3,7,111,13,4,24,4,8]

print(A[zadanie1_1(A,n)])
