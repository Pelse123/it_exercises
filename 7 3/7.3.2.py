def szyfr_cezara(szyfrogram,klucz):
    slowo = ""
    for i in range(len(szyfrogram)):
        if ord(szyfrogram[i])>=65 and ord(szyfrogram[i])<=90:
            slowo = slowo + chr(((ord(szyfrogram[i])-ord("A")-klucz)%26)+ord("A"))
    return slowo


plik = open("dane_6_2.txt","r")
zapis = open("wyniki_6_2.txt","w")

k = 107
for linia in plik:
    szyfr,klucz = linia.strip().split()
    zapis.write(szyfr_cezara(szyfr,int(klucz))+"\n")


plik.close()
zapis.close()