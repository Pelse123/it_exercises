

"""
i = 0
A=[1,4,2,7,8]
w = 0
x = 4
licznik1_petli = 0
licznik2_petli = 0
while i<=4:
    sk = A[i]
    j =4-i
    while j>0:
        sk = sk*x
        j = j-1
        licznik2_petli +=1
    w = w+sk
    i=i+1
    licznik1_petli = licznik1_petli+1
print(w)
print(licznik1_petli)
print(licznik2_petli)

"""
i = 0
A=[1,4,2,7,8]
w = A[0]
x = 4
licznik1_petli = 0
licznik2_petli = 0
while i<4:
    i = i+1
    w=w*x + A[i]
    licznik1_petli = licznik1_petli+1
    licznik2_petli = licznik2_petli+1
print(w)
print(licznik1_petli)
print(licznik2_petli)
