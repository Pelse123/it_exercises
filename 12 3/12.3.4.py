n = int(input())

while n<2:
    n = int(input())

T=[0]*(n+1)
T[0]=False
i = 1

while i<=n:
    T[i] = int(input())
    i+=1
m = 0

wmaks = 0
i = 1
wmin = T[1]
while i<=n:
    if T[i]>wmaks:
        wmaks = T[i]
    if T[i]<wmin:
        wmin = T[i]
    i=i+1

if wmin<0:
    wmaks += wmin*(-1)

Tm = [0]*(wmaks+2)
Tm[0]=False
Tl = [0]*(wmaks+2)
Tl[0]=False
i = 1

i = 1
while i<=wmaks+1:
    Tl[i] = wmin
    wmin+=1
    i+=1

i = 1

while i<=n:
    j = 1
    while j<=wmaks+1:
        if T[i]==Tl[j]:
            Tm[j]+=1
        j+=1
    i+=1

i = 1

while i<=wmaks+1:
    if Tm[i]>Tm[m]:
        m = i
    i+=1

print(Tl[m])
