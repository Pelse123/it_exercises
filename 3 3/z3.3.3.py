"""n = int(input())
pierwszy = 0
drugi = 1
if n == 0:
    print(pierwszy)
elif n == 1:
    print(drugi)
else:
    for i in range(2, n + 1):
        wynik = pierwszy + drugi
        pierwszy = drugi
        drugi = wynik
        print(wynik,end=" ")"""

n = int(input())
pierwszy = 0
drugi = 1
i = 2
if n == 0:
    print(pierwszy)
elif n == 1:
    print(pierwszy,drugi)
else:
    print(pierwszy, drugi,end=" ")
    while i<=n:
        wynik = pierwszy + drugi
        pierwszy = drugi
        drugi = wynik
        i = i + 1
        print(wynik,end=" ")