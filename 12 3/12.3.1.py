A=[False,1,1,1,2,3,4,5,6]
n = len(A)
C=[0]*n
C[0]=False
for i in range(1,n):
    C[i]=1
    for j in range(1,i):
        if A[j] < A[i] and C[j]+1 > C[i]:
            C[i] = C[j]+1
print(C)