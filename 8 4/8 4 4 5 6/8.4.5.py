plik= open('mecz.txt', 'r')
zapis= open('wyniki1.txt', 'w')

linia = plik.readline().strip()

A = 0
B = 0


for i in range(len(linia)):
    if linia[i] == 'A':
        A += 1
    if linia[i] == 'B':
        B += 1
    if A>=1000 and abs(A-B)>=3:
        break
    if B>=1000 and abs(A-B)>=3:
        break

zapis.write("b)\n")
ktora_druzyna_wygrala = ""
if A>B:
    ktora_druzyna_wygrala = "A"
else:
    ktora_druzyna_wygrala = "B"
zapis.write(ktora_druzyna_wygrala+" "+str(A)+":"+str(B))


zapis.close()
plik.close()