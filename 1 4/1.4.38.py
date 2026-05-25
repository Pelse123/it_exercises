def sylvester(n):
    if n<2:
        return 2
    wyraz = 1
    for i in range(1,n):
        wyraz = wyraz*sylvester(i)
    return wyraz+1


n = int(input())
for i in range(1,n+1):
    print(sylvester(i))

def sylveste(n):
    tablica = [2]
    kolejny_wyraz = 1
    for i in range(n-1):
        kolejny_wyraz = kolejny_wyraz * tablica[i]
        tablica.append(kolejny_wyraz+1)
    return tablica

print(sylveste(6))