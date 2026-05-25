a = int(input())
b = int(input())
if b == 0:
    print("Nie można dzielić przez 0!")
    quit()
if (a%b)==0:
    print(f"Liczba {a} jest podzielna przez {b}")
else:
    print(f"Liczba {a} nie jest podzielna przez {b}")
