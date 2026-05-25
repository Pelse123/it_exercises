def przestawieniowy_odszyfruj(napis):
    szyfrogram = ""
    for i in range(0,len(napis),2):
        if i+2 > len(napis):
            szyfrogram += napis[i]
            break
        szyfrogram += napis[i+1]+napis[i]

    return szyfrogram
slowko = input()
print(przestawieniowy_odszyfruj(slowko))