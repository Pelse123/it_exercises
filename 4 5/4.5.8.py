def znajdz_najczestrza_literke(napis):
    alfabet = [0]*26
    for i in range(len(napis)):
        if ord(napis[i])>=ord('a') and ord(napis[i])<=ord('z'):
            alfabet[ord(napis[i])-ord('a')] += 1
        elif ord(napis[i])>=ord('A') and ord(napis[i])<=ord('Z'):
            alfabet[ord(napis[i]) - ord('a')] += 1
    maks = 0
    maks_i = 0
    for i in range(len(alfabet)):
        if maks<alfabet[i]:
            maks = alfabet[i]
            maks_i = i
    return maks_i+ord('a')

def odszyfruj(tekst):
    najczestrza = znajdz_najczestrza_literke(tekst)
    odszyfrowany = ""
    klucz = (najczestrza - ord('a'))%26
    for i in range(len(tekst)):
        odszyfrowany += chr((ord(tekst[i])-klucz-ord('a'))%26 + ord('a'))
    return odszyfrowany



tekst = input()
print(odszyfruj(tekst))