def szyfr_cezara(slowo,klucz):
    szyfrogram = ""
    for i in range(len(slowo)):
        if ord(slowo[i])>=65 and ord(slowo[i])<=90:
            szyfrogram = szyfrogram + chr(((ord(slowo[i])-ord("A")+klucz)%26)+ord("A"))
    return szyfrogram

plik = open("dane_6_1.txt","r")
zapis = open("wyniki_6_1.txt","w")

k = 107
for linia in plik:
    zapis.write(szyfr_cezara(linia.strip(),k)+"\n")

plik.close()
zapis.close()