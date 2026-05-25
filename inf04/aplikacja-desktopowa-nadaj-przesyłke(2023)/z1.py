"""
****************************************************
 nazwa funkcji: sito_eratostenesa
 parametry wejściowe: wypelnienie_wartosci_tablicy - tablica która przyjmuje same wartości True
 wartość zwracana: brak
 informacje: Funkcja zamienia wartości true na false jeśli liczba nie jest pierwsza metodą sita erastotenesa
 autor: 694202137
****************************************************
"""
def sito_eratostenesa(wypelnienie_wartosci_tablicy):
    n = len(wypelnienie_wartosci_tablicy)-1
    for i in range(2,int(n**(1/2))+1):
        for j in range(2*i,n+1,i):
            wypelnienie_wartosci_tablicy[j] = False

n = 100
tablica_erastotenesa = [True] * (n + 1)
tablica_erastotenesa[0] = False
tablica_erastotenesa[1] = False
sito_eratostenesa(tablica_erastotenesa)


for i in range(n+1):
    if tablica_erastotenesa[i]:
        print(i, end=" ")


