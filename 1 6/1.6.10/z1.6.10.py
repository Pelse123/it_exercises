def sprawdz_napis(napis):
    pierwszy_znak = napis[0]
    for i in range(len(napis)):
        if napis[i] != pierwszy_znak:
            return False
    return True

plik = open("napisy.txt", "r")
zapis = open("zadanie4.txt", "w")
ilosc_zer = 0
ilosc_jedynek = 0
for linia in plik:
    if sprawdz_napis(linia.strip()):
        if linia[0] =="0":
            ilosc_zer = ilosc_zer + 1
        elif linia[0] =="1":
            ilosc_jedynek = ilosc_jedynek + 1

zapis.write(f"c)\nLiczba napisow z samymi 0: {ilosc_zer}\nLiczba napisow z samymi 1: {ilosc_jedynek}")

plik.close()
zapis.close()
