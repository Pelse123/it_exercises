def funkcja(tekst,liczba):
    tablica = tekst.split(" ")
    zdanie_na_10 = ""
    for i in range(len(tablica)):
        if len(zdanie_na_10)+len(tablica[i])>liczba:
            print(zdanie_na_10)
            zdanie_na_10 =""
        zdanie_na_10 += tablica[i] + " "
    print(zdanie_na_10)


tekst = input()
liczba = int(input())
funkcja(tekst,liczba)



