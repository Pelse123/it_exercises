
mk = 10
n = int(input())
Masa=[0]*(n+1)
Masa[0]=False
Cena=[0]*(n+1)
Cena[0]=False

for i in range(1,n+1):
    Masa[i] = int(input())
    while (Masa[i] < 0):
        Masa[i] = int(input())

for i in range(1,n+1):
    Cena[i] = int(input())
    while (Cena[i] <= 0):
        Cena[i] = int(input())

K=[0]*(n+1)
K[0]=False
w = 0
i = 1
while i<=n and mk>0:
    if mk//Masa[i]>=1:
        K[i]=1
        mk=mk-Masa[i]
    else:
        K[i]=mk//Masa[i]
        mk=mk%Masa[i]
    w = w + K[i]*Cena[i]
    i+=1

print(w)
