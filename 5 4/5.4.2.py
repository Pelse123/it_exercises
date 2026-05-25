def Vigenere_odszyfruj(tekst,klucz):
    tekst_jawny= ""
    for i in range(len(tekst)):
        przesuniecie = (ord(tekst[i])-ord("A") - ord(klucz[i%len(klucz)]) - ord("A"))%26
        tekst_jawny = tekst_jawny + chr(przesuniecie+ord("A"))
    return tekst_jawny

szyfrogram = input()
klucz = input()

print(Vigenere_odszyfruj(szyfrogram,klucz))

