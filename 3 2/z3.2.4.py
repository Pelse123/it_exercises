a  = 6
b = 7
wynik = 0
while b>0:
    if b%2 == 1:
        wynik = wynik + a
    a = a+a
    b = b//2
print(wynik)