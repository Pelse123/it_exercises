a = int(input())
ostatnia_liczba  = 0
suma = 0
while (a!=0):
    if(a%2!=0):
        ostatnia_liczba = a%10
        suma = suma + ostatnia_liczba
    a = a // 10


print(suma)