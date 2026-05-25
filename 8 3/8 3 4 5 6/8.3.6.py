# A=1, C=2, G=3, T=4

def waga_sekwencji(sekwencja):
    waga = 0
    tablica = ["A","C","G","T"]
    for i in range(len(sekwencja)):
        for j in range(len(tablica)):
            if sekwencja[i] == tablica[j]:
                waga += j+1
    return waga

plik = open("dna_sekwencje.txt","r")
zapis = open("wyniki_dna.txt","w")
zapis.write("3)\n")
maks_suma = 0
wynik = ""

for linia in plik:
    if waga_sekwencji(linia.strip())>maks_suma:
        maks_suma = waga_sekwencji(linia.strip())
        wynik = linia.strip()

zapis.write(f"{wynik}\n{maks_suma}\n")
zapis.close()
plik.close()

