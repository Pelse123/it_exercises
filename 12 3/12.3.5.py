w = int(input())
k = int(input())
n = int(input())

dzi=n
dln  = 0

while dzi>0:
    dln += 1
    dzi=dzi//2

T=[0] * dln

dzi = n
n = 0
i = 0
while dzi>0:
    T[dln-i-1]=dzi%2
    dzi=dzi//2
    i+=1

i = 0
while i<dln:
    n = n*10 + T[i]
    i=i+1

x=0
if w*k%dln == 0:
    x = n%10
else:
    wystaje = dln-(w*k%dln)
    while wystaje>=0:
        x = n%10
        wystaje=wystaje-1
        n=n//10

print(x)