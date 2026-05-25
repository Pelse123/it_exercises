def suma_liczb(n):
    suma = 0
    for i in range(n+1):
        suma +=i
    return suma

liczba = int(input())
print(suma_liczb(liczba))