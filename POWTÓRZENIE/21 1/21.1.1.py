def czy_palindromiczna(liczba):
    if len(liczba)<2:
        return False
    else:
        for i in range(len(liczba)//2):
            if liczba[i] != liczba[len(liczba)-i-1]:
                return False
    return True

tablica_liczb = []
miejsca_w_tablicy = int(input())
for i in range(miejsca_w_tablicy):
    tablica_liczb.append(input())

for i in range(miejsca_w_tablicy):
    liczba = int(tablica_liczb[i])
    if czy_palindromiczna(str(liczba-1))or czy_palindromiczna(str(liczba+1)):
        print(tablica_liczb[i])
