x = 210
wynik = 0
i = 2
while i*i<=x:
    if x%i==0:
        wynik = wynik+1
    i = i+1
print(wynik)