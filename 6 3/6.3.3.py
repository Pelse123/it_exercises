dane ={'imie':'Jan', 'nazwisko':'Kowalski', 'wiek':34, 'miejsce-zamieszkania':'Warszawa'}
dane.pop('wiek')
dane['miejsce-zameldowania'] = 'Sopot'
for klucz in dane:
    wartosc = dane[klucz]
    print(klucz,":", wartosc)
