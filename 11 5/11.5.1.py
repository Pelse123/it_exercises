d = int(input())
while d<1:
    d=int(input())
Bin = [0] * (d+1)
Bin[0]=False
for i in range(1,d+1):
    Bin[i]=int(input())
x = 0

for i in range(2,d+1):
    if Bin[1]==1:
        if Bin[i]==0:
            x = x+2**(d-i)
    else:
        if Bin[i]==1:
            x = x + 2 ** (d - i)

if Bin[1]==1:
    x = x*(-1)
print(x)



