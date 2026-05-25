
napis = input()
znak = input()
duzyznak = 0
malyznak = 0
ilosc = 0
if(ord(znak)>=97):
    duzyznak = chr(ord(znak)-32)
    malyznak = znak
else:
    duzyznak = znak
    malyznak = chr(ord(znak)+32)

for i in range(len(napis)):
    if(duzyznak==napis[i] or malyznak==napis[i]):
        ilosc=ilosc+1

print(ilosc)
