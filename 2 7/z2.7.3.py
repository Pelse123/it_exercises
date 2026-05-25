def wplata():
    try:
        ilosc_wplaty = int(input("Podaj ilość wpłaty: "))
        if ilosc_wplaty<0:
            raise ValueError
    except ValueError:
        print("Dane zostały wprowadzone nieprawidłowo!")
        return 0
    return ilosc_wplaty

def wyplata(ilosc):
    try:
        ilosc_wyplaty = int(input("Podaj ilość wypłaty: "))
        if ilosc_wyplaty<0:
            raise ValueError
        if ilosc_wyplaty>ilosc:
            raise TypeError(f"Operacja nie może zostać przeprowadzona. Za mało środków na koncie. (SALDO:{ilosc})(WYPŁACANA WARTOŚĆ: {ilosc_wyplaty})")
    except ValueError:
        print("Dane zostały wprowadzone nieprawidłowo!")
        return 0
    except TypeError as e:
        print(e)
        return 0
    return ilosc_wyplaty

def sprawdzenie_salda(ilosc):
    print(f"Saldo: {ilosc}zł")


ilosc_gotowki = 1000


try:
    petla = 1
    while petla != 0:
        jaka_operacja = int(input("Jaką operacje chcesz wykonać? \n 1.Sprawdzenie salda \n 2.Wpłata gotówki \n 3.Wypłata gotówki \n 0.wyjdz \n"))
        if jaka_operacja > 3 or jaka_operacja < 0:
            raise TypeError("Niepoprawny zakres operacji")
        if jaka_operacja == 1:
            sprawdzenie_salda(ilosc_gotowki)
        if jaka_operacja == 2:
            ilosc_gotowki = ilosc_gotowki + wplata()
        if jaka_operacja == 3:
            ilosc_gotowki = ilosc_gotowki - wyplata(ilosc_gotowki)
        if jaka_operacja == 0:
            petla = 0
except ValueError:
    print("Niepoprawny znak, wpisz liczbę!")
except TypeError as e:
    print(e)