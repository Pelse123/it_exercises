def szyfr_cezara(slowo,klucz):
    szyfrogram = ""
    for i in range(len(slowo)):
        if ord(slowo[i])>=65 and ord(slowo[i])<=90:
            szyfrogram = szyfrogram + chr(((ord(slowo[i])+ord("A")+klucz)%26)+ord("A"))
    return szyfrogram

def oblicz_roznice_kluczy(slowo1,slowo2):
    return ord(slowo2[0])-ord(slowo1[0])

def czy_takie_same_slowa(slowo,szyfr,roznica):
    if szyfr_cezara(slowo,roznica) != szyfr:
        return False
    return True

plik = open("dane_6_3.txt","r")
zapis = open("wyniki_6_3.txt","w")

for linia in plik:
    slowo,zaszyfrowane = linia.strip().split()
    roznica = oblicz_roznice_kluczy(slowo,zaszyfrowane)

    if czy_takie_same_slowa(slowo,zaszyfrowane,roznica)==False:
        zapis.write(slowo+"\n")



plik.close()
zapis.close()