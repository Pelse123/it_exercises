napis = input()

for i in range(ord('a'), ord('z')+1):
    ilosc = 0
    znak = chr(i)

    if((ord(znak)>=97) and (ord(znak)<=122)):
        duzyznak = chr(ord(znak)-32)
        malyznak = znak
    elif((ord(znak)>=65) and (ord(znak)<=90)):
        duzyznak = znak
        malyznak = chr(ord(znak)+32)

    for j in range(len(napis)):
        if(duzyznak==napis[j] or malyznak==napis[j]):
            ilosc = ilosc+1
    if(ilosc!=0):
        print(f"{znak}:{ilosc}")


