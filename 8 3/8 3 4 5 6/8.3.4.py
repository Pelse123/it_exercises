def palindrom_genetyczny(sekwencja):
    sekwencja2 = ""
    for i in range(len(sekwencja)):
        if sekwencja[i] == "A":
            sekwencja2 += "T"
        elif sekwencja[i] == "T":
            sekwencja2 += "A"
        elif sekwencja[i] == "C":
            sekwencja2 += "G"
        elif sekwencja[i] == "G":
            sekwencja2 += "C"
    for i in range(len(sekwencja2)):
        if sekwencja[len(sekwencja) - 1 - i] != sekwencja2[i]:
            return False
    return True

plik = open("dna_sekwencje.txt","r")
zapis = open("wyniki_dna.txt","w")

licznik = 0
naj_pali = ""
dlugosc = 0

for liczba in plik:
    if palindrom_genetyczny(liczba.strip()):
        licznik += 1
        if len(liczba.strip())>dlugosc:
            dlugosc = len(liczba.strip())
            naj_pali = liczba.strip()

zapis.write("1)\n")
zapis.write(f"{licznik}\n")
zapis.write(f"{naj_pali}\n")
zapis.write(f"{dlugosc}\n")

zapis.close()
plik.close()