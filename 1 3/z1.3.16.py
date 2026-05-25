"""napis = input()
alfabet = []
iloscwystapien=[0]*26
for i in range(ord('a'), ord('z')+1):
    alfabet.append(chr(i))

for i in range(26):
    for j in range(len(napis)):
        if napis[j] == alfabet[i] or napis[j] == chr(ord(alfabet[i])-32):
            iloscwystapien[i] = iloscwystapien[i] +1
czytak = True

for i in range(len(iloscwystapien)):
    if iloscwystapien[i] == 0:
        czytak = False
if czytak:
    print("Tak")
else:
    print("Nie")"""

napis = input()
alfabet = []
iloscwystapien=[]
for i in range(ord('a'), ord('z')+1):
    alfabet.append(chr(i))
flaga = True
for i in range(26):
    licznik = 0
    for j in range(len(napis)):
        if napis[j] == alfabet[i] or napis[j] == chr(ord(alfabet[i])-32):
            licznik = licznik + 1
    if licznik == 0:
        print("Nie")
        flaga = False
        break
if(flaga):
    print("Tak")

