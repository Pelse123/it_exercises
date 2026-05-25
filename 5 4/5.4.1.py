def Vigenere(tekst,klucz):
    szyfrogram = ""
    for i in range(len(tekst)):
        przesuniecie = (ord(tekst[i])-ord("A") + ord(klucz[i%len(klucz)]) - ord("A"))%26
        szyfrogram = szyfrogram + chr(przesuniecie+ord("A"))
    return szyfrogram

tekst_jawny = input()
klucz = input()

print(Vigenere(tekst_jawny,klucz))

