def zamien_na_liczbe(znak):
    if ord(znak)>=ord("A"):
        return ord(znak) - 55
    else:
        return int(znak)

def schemat_hornera(system,liczba):
    wynik = liczba[0]
    for i in range(1,len(liczba)):
        wynik = system * wynik + liczba[i]
    return wynik

system = int(input())
liczba = input()
liczba_lista=[]
for i in range(len(liczba)):
    liczba_lista.append(zamien_na_liczbe(liczba[i]))
print(schemat_hornera(system,liczba_lista))