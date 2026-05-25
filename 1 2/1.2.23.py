a = int(input())
modulo = 0
modulo2 = a % 10
liczba = 0
while(a!=0):
    modulo = a % 10
    liczba = liczba*10 + modulo
    a = a//10
print(liczba)

