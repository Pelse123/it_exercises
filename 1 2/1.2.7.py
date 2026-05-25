a = int(input())
b = int(input())
suma = 0
while(a>b):
    a = int(input())
    b = int(input())
for i in range(a,b+1,3):
    print(i)
    suma = suma + i
print(suma)