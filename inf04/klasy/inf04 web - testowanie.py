from inf04web import *

print(f"Liczba zarejestrowanych osób to {Osoba.static}")

obiekt1 = Osoba()

id = input("Podaj id: ")
imie = input("Podaj imie: ")
obiekt2 = Osoba(id,imie)

obiekt3 = obiekt2.kopiuj()

obiekt1.wypisz("Jan")
obiekt2.wypisz("Jan")
obiekt3.wypisz("Jan")

print(f"Liczba zarejestrowanych osób to {Osoba.static}")