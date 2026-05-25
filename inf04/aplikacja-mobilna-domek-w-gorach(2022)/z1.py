import random

def wypelnij_tablice(tab,n):
    for i in range(n):
        tab.append(random.randint(1,100))
"""
******************************************************
 nazwa funkcji: szukanie_z_wartownikiem
 argumenty: tab - tablice wypełnioną losowymi wartościami
    szukana - liczba wpisana od użytkownika która jest szukana w tablicy
 typ zwracany: indeks szukanej wartości jeśli znajduje się w tablicy
 w przeciwnym wypadku False
 informacje: Funkcja znajduje szukany element za pomocą metody z wartownikiem
 autor: 000000000000000000
*****************************************************
"""
def szukanie_z_wartownikiem(tab,szukana):
    n = len(tab)
    tab.append(szukana)
    i = 0
    while tab[i]!=szukana:
        i+=1
    if i == n:
        return False
    else:
        return i



n = int(input("Podaj ilość miejsc: "))
while n<50:
    n = int(input("Podaj ilość miejsc (minimum 50): "))
szukana = int(input("Podaj liczbę szukaną: "))
tab = []
wypelnij_tablice(tab,n)
for i in range(n):
    if i!=n-1:
        print(tab[i],end=",")
    else:
        print(tab[i])
wynik = szukanie_z_wartownikiem(tab,szukana)
if wynik==False:
    print("Brak szukanej wartości")
else:
    print(F"Znaleziona wartość {tab[wynik]} - i:{wynik}")