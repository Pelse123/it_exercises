#A[1...k] == B[n-k+1...n] and A[k+1...n] =B[1..n-k]

def czy_k_podobne(n,A,B,k):
    i = 1
    while i<=k:
        if A[i]!=B[n-k+i-1]:
            return False
        i+=1
    i = 1
    while i<=n-k-1:
        if A[k+i]!=B[i]:
            return False
        i+=1
    return True


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

k = int(input())
while k<0 or k>n:
    k = int(input())
if czy_k_podobne(n,A,B,k):
    print("PRAWDA")
else:
    print("FAŁSZ")