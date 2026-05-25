def s(k):
    temp_k = k
    wynik = 0
    while temp_k > 0:
        wynik = wynik + temp_k%10
        temp_k = temp_k // 10
    return wynik

n = 0
flaga = True
while n<1000 or n>9999:
    n = int(input())

for i in range(n):
    k = i
    wynik = k+s(k)
    if wynik == n:
        flaga = False
        print(k)
        break
if flaga:
    print("NIE")





