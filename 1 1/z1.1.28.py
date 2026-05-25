print("--------------------------------------------------------")
print("KALKULATOR - WYBIERZ LICZBE PRZYPISANĄ DO DZIALANIU")
print("1.Dodawanie")
print("2.Odejmowanie")
print("3.Mnożenie")
print("4.Dzielenie")
print("5.Potęgowanie")
print("6.Pierwiastkowanie")
print("--------------------------------------------------------")

liczba = int(input())

if liczba == 1:
    print("Wybrano dodawanie")
    a = int(input("Podaj składnik: "))
    b = int(input("Podaj 2 składnik: "))
    wynik = a+b
    print(f"Suma dodawania liczby {a} i {b} wynosi: {wynik}")
elif liczba == 2:
    print("Wybrano odejmowanie")
    a = int(input("Podaj odjemną: "))
    b = int(input("Podaj odjemnik: "))
    wynik = a-b
    print(f"Różnica odejmowania liczby {a} i {b} wynosi: {wynik}")
elif liczba == 3:
    print("Wybrano mnożenie")
    a = int(input("Podaj czynnik: "))
    b = int(input("Podaj 2 czynnik: "))
    wynik = a*b
    print(f"Iloczyn mnożenia liczby {a} i {b} wynosi: {wynik}")
elif liczba == 4:
    print("Wybrano dzielenie")
    a = int(input("Podaj dzielną: "))
    b = int(input("Podaj dzielnik: "))
    if(b==0):
        print("Nie można dzielić przez 0!")
    else:
        wynik = a/b
        print(f"Iloraz dzielenia liczby {a} i {b} wynosi: {wynik}")
elif liczba == 5:
    print("Wybrano potęgowanie")
    a = int(input("Podaj podstawę: "))
    b = int(input("Podaj wykładnik: "))
    wynik = a**b
    print(f"Potęga potęgowania liczby {a} do {b} wynosi: {wynik}")
elif liczba == 6:
    print("Wybrano pierwiastkowanie")
    a = int(input("Podaj liczbę pierwiastkowaną: "))
    b = int(input("Podaj stopień: "))
    wynik = a**(1/b)
    print(f"Wynik pierwiastkowania {b} stopnia liczby {a} wynosi: {wynik}")
else:
    print(f"Wybrano {liczba} wybierz liczby z przedziału 1 - 6")


