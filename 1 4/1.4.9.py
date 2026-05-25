def suma_cyfr(n):
    suma = 0
    while n!=0:
        suma += n%10
        n = n//10
    return suma

liczba = int(input())
print(suma_cyfr(liczba))