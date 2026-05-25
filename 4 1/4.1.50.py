n = int(input())
wynik = 0
for i in range(n):
    wynik = (wynik<<1)|1
print(wynik)