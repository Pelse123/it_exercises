maks = 1
nr = 1

A=[False,1,1,1,1,1,1,1,1,1,1,1]
n = len(A)

for i in range(1,n):
    k = 0
    for j in range(i,n):
        if A[i]==A[j]:
            k = k+1
    if k>maks:
        print("l")
        maks = k
        nr = i

