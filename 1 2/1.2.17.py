a = int(input())
b = int(input())
while(a>b):
    a = int(input())
    b = int(input())
i = a
suma = 0
while(i<=b):
    print(i)
    suma = suma +i
    i = i + 3
print(suma)