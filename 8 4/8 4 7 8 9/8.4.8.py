def czy_palindrom(slowo):
    for i in range(0,len(slowo)//2):
        if slowo[i] != slowo[len(slowo)-i-1]:
            return False
    return True

plik= open('identyfikator.txt', 'r')
zapis= open('wyniki4_1.txt', 'w')

for linia in plik:
    id = linia.strip()
    numer = ""
    seria = ""
    for i in range(3,len(id)):
        numer += id[i]
    for i in range(0,3):
        seria += id[i]
    if czy_palindrom(seria) or czy_palindrom(numer):
        zapis.write(id+"\n")

zapis.close()
plik.close()