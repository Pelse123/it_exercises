n = int(input())
suma = 0
while n>0:
    suma = suma + n%10
    n = n//10
print(suma)

"""
1. przypisz zmiennej suma wartość 0
2. Dopóki n jest mniejsze od 0 wykonuj:
    2.1 przypisz zmiennej suma wartość suma + n mod 10
    2.2 przypisz zmiennej n wartość n div 10
3. wypisz wartość suma
"""