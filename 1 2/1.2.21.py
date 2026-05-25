a = int(input())
ostatnia_liczba = 0
while(a!=0):
    ostatnia_liczba  = a%10
    print(ostatnia_liczba**2, end=" ")
    a=a//10