def nieparzysty_skrot(n):
    tm = 0
    while n > 0:
        o = n % 10
        if o % 2 != 0:
            tm = tm * 10 + o
        n = n // 10

    if tm > 0:
        m = 0
        while tm > 0:
            m = m * 10 + tm % 10
            tm = tm // 10
        return m
    else:
        return 0

def nwd(a,b):
    while b>0:
        a,b = b,a%b
    return a
plik = open('skrot2.txt', 'r')
zapis = open('wyniki3_2.txt', 'w')

for linia in plik:
    liczba = int(linia.strip())
    liczba_nieparzysty = nieparzysty_skrot(liczba)
    if nwd(liczba,liczba_nieparzysty) == 7:
        zapis.write(str(liczba)+"\n")

zapis.close()
plik.close()