def algorytm_najwieksze_pole_powierzchni(n,A,p):
    i = 0
    S = 0
    while i<n:
        j = 0
        while j<n:
            if i != j:
                w = A[i]*A[j]
                if w%p != 0:
                    if w>S:
                        S = w
            j = j+1
        i = i+1
    return S


n = int(input())

while n < 0:
    n = int(input())
A=[0]*n
i = 0

while n>i:
    A[i]=int(input())
    i=i+1

p = int(input())

S = algorytm_najwieksze_pole_powierzchni(n,A,p)
print(S)