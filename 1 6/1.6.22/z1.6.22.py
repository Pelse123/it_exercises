plik = open("liczby2.txt", "r")
zapis = open("wyniki3.txt", "w")
zapis.write("a)\n")
for linia in plik:
    zapis.write(f"{int(linia.strip())**2}\n")
plik.close()
zapis.close()