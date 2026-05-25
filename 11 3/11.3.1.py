def dzielniki(a):
    i = 2
    suma = 1
    while i*i<a:
        if a % i == 0:
            suma += i
            if a%(a//i)==0:
                suma = suma+a//i
        i += 1
    return suma-1

a = int(input())
while a<0:
    a = int(input())
b = dzielniki(a)
if   dzielniki(b) == a:
    print(b)
else:
    print("NIE")


