def mozliwe_kwadraty(kwadrat):
    gwiazdka = [
        ["*","*","*"],
        ["*","*","*"],
        ["*","*","*"]
    ]
    kolko =[
        ["o", "o", "o"],
        ["o", "o", "o"],
        ["o", "o", "o"]
    ]
    plusik =[
        ["+", "+", "+"],
        ["+", "+", "+"],
        ["+", "+", "+"]
    ]
    if kwadrat == gwiazdka or kwadrat == kolko or kwadrat == plusik:
        return True
    return False

"""
ij-1 ij ij+1
"""


def znajdz_kwadrat(tablica):
    ilosc = 0
    miejsca = ""
    for i in range(1,len(tablica)-1):
        for j in range(1,len(tablica[i])-1):
            kwadrat = [
                [tablica[i-1][j-1],tablica[i-1][j],tablica[i-1][j+1]],
                [tablica[i][j-1], tablica[i][j], tablica[i][j+1]],
                [tablica[i+1][j-1], tablica[i+1][j], tablica[i+1][j + 1]]
            ]
            if mozliwe_kwadraty(kwadrat):
                ilosc+=1
                miejsca = miejsca + str(i+1) +" "+ str(j+1) + " "
    return miejsca,ilosc



plik = open("symbole.txt","r")
macierz_znakow = []
for linia in plik:
    wiersz = []
    for i in linia.strip():
        wiersz.append(i)
    macierz_znakow.append(wiersz)

miejsca,ilosc = znajdz_kwadrat(macierz_znakow)
print(ilosc,miejsca)

plik.close()