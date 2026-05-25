tekst = input()
klucz = input()
powiel = klucz
while len(tekst)>len(klucz):
    klucz = klucz + powiel

wynik=""
tablica_liczb = []
for i in range(len(tekst)):
    if tekst[i] != " ":
        wynik = wynik + tekst[i]
    else:
        tablica_liczb.append(int(wynik))
        wynik = ""
    if i == len(tekst)-1:
        tablica_liczb.append(int(wynik))

for i in range(len(tablica_liczb)):
    print(chr(tablica_liczb[i]^ord(klucz[i])), end="")