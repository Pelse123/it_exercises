def tablica_pierwszych(n):
    tablica_pierwszych = []
    for i in range(2, n):
        czypierwsza = True
        for j in range(2, i):
            if i % j == 0:
                czypierwsza = False
                break
        if czypierwsza:
            tablica_pierwszych.append(i)
    return tablica_pierwszych

def czy_suma_dwoch_pierwszych(n,tablica_pierwszych):
    for i in range(len(tablica_pierwszych)):
        for j in range(len(tablica_pierwszych)):
            if(tablica_pierwszych[j] != tablica_pierwszych[i]):
                if(tablica_pierwszych[i] + tablica_pierwszych[j] == n):
                    return True
    return False


naturalna = int(input())
tablica = tablica_pierwszych(naturalna)
if(czy_suma_dwoch_pierwszych(naturalna, tablica)):
    print("Tak")
else:
    print("Nie")
