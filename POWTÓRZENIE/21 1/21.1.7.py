def czy_podzielna_przez_2(liczba):
    if liczba%2==0:
        return True
    else:
        return False

def czy_podzielna_przez_8(liczba):
    if liczba%8==0:
        return True
    else:
        return False

def potega_liczby(podstawa,potega):
    wynik = 1
    i = 0
    while i!=potega:
        wynik *=podstawa
        i+=1
    return wynik


def zamien_2_na_10(liczba_2):
    liczba_10 = 0
    i = 0
    while liczba_2!=0:
        potega = potega_liczby(2,i)
        liczba_10 += potega*(liczba_2%10)
        i +=1
        liczba_2=liczba_2//10
    return liczba_10

plik = open("liczby.txt","r")
zapis = open("wynik4.txt","w")

tablica = [0,0]
for liczba in plik:
    na_10 = zamien_2_na_10(int(liczba.strip()))
    if czy_podzielna_przez_2(na_10):
        tablica[0] += 1
    if czy_podzielna_przez_8(na_10):
        tablica[1] += 1

zapis.write(f"2)\nLiczb podzielnych przez 2: {tablica[0]}\nLiczb podzielnych przez 8: {tablica[1]}")

zapis.close()
plik.close()



