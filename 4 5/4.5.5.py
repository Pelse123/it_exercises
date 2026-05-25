def cezar_odszyfruj(napis,klucz):
    szyfrogram = ""
    klucz = klucz%26
    for i in range(len(napis)):
        if ord(napis[i])>=ord('a') and ord(napis[i])<=ord('z'):
            szyfrogram = szyfrogram + chr((ord(napis[i])-klucz-ord("a"))%26+ord('a'))
        elif ord(napis[i])>=ord('A') and ord(napis[i])<=ord('Z'):
            szyfrogram = szyfrogram + chr((ord(napis[i])-klucz-ord("A"))%26+ord('A'))
        else:
            szyfrogram = szyfrogram + napis[i]
    return szyfrogram

napis = input()
klucz = int(input())
print(cezar_odszyfruj(napis,klucz))