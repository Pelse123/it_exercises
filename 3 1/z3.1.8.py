A = [5, 6, 8, 10,12]
B = [8, 9, 10, 11,13]
n = len(A)
i = 0
j = n-1
x = 20
l = 0
flaga = False
while i < n and j>=0:
    l+=1
    if A[i]+B[j] == x:
        flaga = True
        break
    else:
        if A[i]+B[j] < x:
            i = i+1
        else:
            j = j-1
print(flaga)
print(l)
