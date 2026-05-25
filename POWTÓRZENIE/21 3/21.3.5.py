def sortowanie_przez_wstawianie(tablica):
    for i in range(1,len(tablica)):
        aktualny = tablica[i]
        j = i-1
        while j>=0 and tablica[j]>aktualny:
            tablica[j+1] = tablica[j]
            j-=1
        tablica[j+1] = aktualny
    return tablica

def wyszukiwanie_wzorca(wzorzec,slowo):
    for i in range(len(slowo)-len(wzorzec)+1):
        ilosc_poprawnych = 0
        for j in range(len(wzorzec)):
            if wzorzec[j]!=slowo[j+i]:
                break
            ilosc_poprawnych += 1

        if ilosc_poprawnych==len(wzorzec):
            return True
    return False


tablica = []
n = int(input())
for i in range(n):
    tablica.append(input())
for i in range(n):
    tablica[i] = sortowanie_przez_wstawianie(list(tablica[i]))


wzorzec = input()

for i in range(n):
    wzorzec_wynik = wyszukiwanie_wzorca(wzorzec,tablica[i])
    if wzorzec_wynik:
        for j in range(len(tablica[i])):
            print(tablica[i][j], end="")
        print()
