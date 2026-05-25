n= int(input())
while n<1:
    n = int(input())
k = int(input())
while k<1:
    k = int(input())
A = []
for i in range(n):
    liczba = int(input())
    while liczba<1 or liczba>k:
        liczba = int(input())
    A.append(liczba)
t = [0]*(k)
for i in range(n):
    pozycja = A[i]-1
    t[pozycja] = t[pozycja]+1

maks_i = 0
for i in range(k):
    if t[maks_i] < t[i]:
        maks_i = i
y = maks_i+1
print(y)