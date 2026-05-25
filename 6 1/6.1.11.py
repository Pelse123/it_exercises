import random
liczba_uzytkownika = 0
liczba_losowa = random.randint(1,100)
while liczba_losowa != liczba_uzytkownika:
    liczba_uzytkownika = int(input())
    if liczba_losowa<liczba_uzytkownika:
        print("Podano za dużą liczbę")
    elif liczba_losowa>liczba_uzytkownika:
        print("Podano za małą liczbę")
    else:
        print("Gratulacje, liczba została odgadnięta")