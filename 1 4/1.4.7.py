def ile_cyfr(n):
    licznik = 0
    while(n!=0):
        n=n//10
        licznik += 1
    return licznik

liczba = int(input())
print(ile_cyfr(liczba))