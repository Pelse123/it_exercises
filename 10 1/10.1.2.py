def czy_pierwsza(liczba):
    if liczba<2:
        return False
    else:
        i = int(liczba**(1/2))+1
        while i>2:
            if liczba%i==0:
                return False
            i=i-1
    return True

def liczba_blizniacza(liczba):
    if czy_pierwsza(liczba)==False:
        return False
    else:
        if czy_pierwsza(liczba-2)==False:
            if czy_pierwsza(liczba+2)==False:
                return False
            else:
                return True
        else:
            return True


liczba = int(input())

while liczba<3:
    liczba = int(input())

if liczba_blizniacza(liczba):
    print("TAK")
else:
    print("NIE")
