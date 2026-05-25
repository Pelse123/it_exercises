def sprawdz_ilosc_zer_i_jedynek(slowo):
    ilosc_jedynek = 0
    ilosc_zer = 0
    for i in range(len(slowo)):
        if slowo[i] == '1':
            ilosc_jedynek += 1
        elif slowo[i] == '0':
            ilosc_zer += 1
    if ilosc_jedynek == ilosc_zer:
        return True
    else:
        return False

plik = open("napisy.txt", "r")
zapis = open("zadanie4.txt", "w")

taka_sama_ilosc= 0
for line in plik:
   if sprawdz_ilosc_zer_i_jedynek(line.strip()):
       taka_sama_ilosc += 1

zapis.write(f"b)\n{taka_sama_ilosc}")

plik.close()
zapis.close()