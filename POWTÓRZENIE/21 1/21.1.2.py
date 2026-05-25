def czy_4_cyfry(liczba):
    licznik = dlugosc_liczby(liczba)
    if licznik>=4:
        return True
    else:
        return False

def dlugosc_liczby(liczba):
    licznik = 0
    while liczba>0:
        liczba=liczba//10
        licznik=licznik+1
    return licznik

def zamien_druga_od_konca_i_druga_od_poczatku(liczba):
    druga_od_poczatku= 0
    druga_od_konca = 0
    index_drugiej_od_poczatku = 2
    index_drugiej_od_konca = dlugosc_liczby(liczba)-1
    licznik = dlugosc_liczby(liczba)
    temp_liczba = liczba

    while licznik>0:
        if licznik == index_drugiej_od_poczatku:
            druga_od_poczatku = temp_liczba%10
        elif licznik == index_drugiej_od_konca:
            druga_od_konca = temp_liczba%10
        temp_liczba=temp_liczba//10
        licznik-=1
    licznik = dlugosc_liczby(liczba)
    wynik_odwrocony = 0
    while licznik>0:
        if licznik == index_drugiej_od_konca:
            wynik_odwrocony = wynik_odwrocony*10+druga_od_poczatku
        elif licznik == index_drugiej_od_poczatku:
            wynik_odwrocony = wynik_odwrocony*10+druga_od_konca
        else:
            wynik_odwrocony = wynik_odwrocony*10+liczba%10
        liczba = liczba//10
        licznik=licznik-1
    return wynik_odwrocony

def odwroc_liczbe(liczba):
    wynik = 0
    while liczba>0:
        wynik = wynik*10+liczba%10
        liczba=liczba//10
    return wynik

liczba = int(input())
while czy_4_cyfry(liczba)==False:
    liczba = int(input())

odwrocony_wynik = zamien_druga_od_konca_i_druga_od_poczatku(liczba)
print(odwroc_liczbe(odwrocony_wynik))


