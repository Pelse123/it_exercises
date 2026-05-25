n = int(input())
temp = 0
while n>0:
    temp = temp*10 + n%10
    n = n//10
n = temp
print(n)

"""
1. przypisz zmiennej temp wartość 0
2. dopóki n>0 wykonuj:
    2.1 przypisz zmiennej temp wartość temp*10 + n mod 10
    2.2 przypisz zmiennej n wartość n div 10
3. przypisz zmiennej n wartość temp
4. wypisz n
"""