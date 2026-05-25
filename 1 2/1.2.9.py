a = int(input())
b = int(input())
k = int(input())
suma=0
while(a>b):
    a = int(input())
    b = int(input())
    k = int(input())
for i in range(a,b+1):
    if((i%k==0) and (i%k**2!=0)):
        suma = suma + i


print(suma)