a = int(input())
ilosc = 0
dodawanie = 0
while(a!=0):
    modulo = a % 10
    ilosc = ilosc+1
    dodawanie = dodawanie + modulo
    a = a//10
print(dodawanie/ilosc)