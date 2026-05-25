plik = open("symbole.txt")
wiersz = ""
for line in plik:
    wiersz = line.strip()
    flaga = True
    for i in range(len(wiersz) // 2):
        if wiersz[i] != wiersz[len(wiersz) - i - 1]:
            flaga = False
            break
                
    if flaga:
        print(wiersz)
plik.close()