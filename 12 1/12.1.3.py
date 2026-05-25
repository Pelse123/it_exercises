def W(j,A):
    if j>1:
        if A[j]<A[j-1]:
            v = A[j]
            A[j] = A[j-1]
            A[j-1] = v
            W(j-1,A)


A=[False,2,4,6,8,10,9,7,5,3,1]
W(8,A)
print(A)

def W_i(j,A):
    i = j
    while i>=2:
        if i>1:
            if A[i]<A[i-1]:
                v = A[i]
                A[i] = A[i-1]
                A[i-1] = v
            else:
                break
        i-=1

A1=[False,2,4,6,8,10,9,7,5,3,1]
W_i(8,A1)
print(A1)