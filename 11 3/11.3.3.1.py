#A[1...k] == B[n-k+1...n] and A[k+1...n] =B[1..n-k]

def czy_k_podobne(n,A,B,k):
    i = 1
    while i<=k:
        if A[i]!=B[n-k+i-1]:
            return False
        i+=1
    i = 1
    while i<n-k:
        if A[k+i]!=B[i]:
            return False
        i+=1
    return True

def czy_podobne(n,A,B):
    for k in range(1,n):
        if czy_k_podobne(n,A,B,k):
            print(k)
            return True
    return False

n = int(input())
while n<0:
    n = int(input())

n=n+1
A=[0]*n
B=[0]*n
i = 1
while i<n:
    A[i] = int(input())
    i+=1
i = 1
while i<n:
    B[i] = int(input())
    i+=1
A[0]=False
B[0]=False

if czy_podobne(n,A,B):
    print("PRAWDA")
else:
    print("FAŁSZ")