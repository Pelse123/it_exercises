def nieparzysty_skrot(n):
    tm = 0
    while n > 0:
        o = n % 10
        if o % 2 != 0:
            tm = tm * 10 + o
        n = n // 10

    if tm > 0:
        return True
    else:
        return False

plik = open('skrot.txt', 'r')
zapis = open('wyniki3_2.txt', 'w')

najwieksza = -1
l = 0
for linia in plik:
    if nieparzysty_skrot(int(linia.strip()))==False:
        l=l+1
        if najwieksza == -1:
            najwieksza = int(linia.strip())
        if najwieksza<int(linia.strip()):
            najwieksza = int(linia.strip())

zapis.write(str(l)+'\n'+str(najwieksza)+'\n')

zapis.close()
plik.close()