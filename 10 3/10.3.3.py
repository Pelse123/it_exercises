n = int(input())
T = []
for i in range(n):
    T.append(input())
temp_licznik = 1
licznik_liter= 1
wynik = 0
for i in range(1,n):
    if T[i-1]==T[i]:
        temp_licznik += 1
    else:
        while temp_licznik != 1:
            wynik += 1
            temp_licznik = temp_licznik//2
        licznik_liter += 1
if T[n-1]!=T[n-2]:
    wynik = wynik+licznik_liter+temp_licznik
else:
    wynik = wynik+licznik_liter
print(wynik)


