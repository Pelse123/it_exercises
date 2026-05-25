def doskonala(l):
    dzielniki = 0
    for i in range(1,(l//2)+1):
        if l%i==0:
            dzielniki = dzielniki+i
    if dzielniki == l:
        print(f"{l} jest liczba doskonala")
    else:
        print(f"{l} nie jest liczba doskonala")


n = int(input())
doskonala(n)