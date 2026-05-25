def nwd(a,b):
    if b==0:
        return a
    return nwd(b,a%b)

def szyfr_cezara(slowo,klucz):
    szyfrogram = ""
    for i in range(len(slowo)):
        if ord(slowo[i]) >= ord('a') and ord(slowo[i]) <= ord('z'):
            szyfrogram += chr((ord(slowo[i])-ord("a") + klucz)%26 + ord('a'))
        elif ord(slowo[i]) >= ord('A') and ord(slowo[i]) <= ord('Z'):
            szyfrogram += chr((ord(slowo[i])-ord("A") + klucz)%26 + ord('A'))
        else:
            szyfrogram += slowo[i]
    return szyfrogram

a = int(input())
b = int(input())
slowo = input()
print(szyfr_cezara(slowo,nwd(a,b)))