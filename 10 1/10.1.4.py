A =[1,2,3,5,4,7,6]
n = len(A)
licznik = 0
for i in range(n):
    m = i
    for j in range(i+1,n):

        if A[m]<A[j]:
            m = j
    if i!=m:
        licznik = licznik+1
        A[i], A[m] = A[m], A[i]
print(A)
print(licznik)