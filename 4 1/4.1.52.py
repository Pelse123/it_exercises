tekst = input()
klucz = input()
powiel = klucz
while len(tekst)>len(klucz):
    klucz = klucz + powiel

for i in range(len(tekst)):
    print(ord(tekst[i])^ord(klucz[i]),end=" ")