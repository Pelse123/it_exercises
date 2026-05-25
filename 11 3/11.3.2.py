def przestaw(A):
    klucz = A[0]
    w = 0
    l = 0
    for k in range(1,len(A)):
        if A[k] < klucz:
            l +=1
            A[w], A[k] = A[k], A[w]
            w = w + 1
    print(w)

A=[10,20,30,40,50,60,70,80,90,100,9,19,29,39,49,59,69,79,89,98,8,18,28,38,48,58,68,78,88,98]
przestaw(A)
print(A)