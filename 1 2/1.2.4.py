a = int(input())
b = int(input())
suma = 0

while(a>b):
    a = int(input())
    b = int(input())

for i in range(a,b+1,1):
    if((i%3==0) and (i%5==0)):
        print(i)
        suma = suma+i

print(f"Suma:{suma}")