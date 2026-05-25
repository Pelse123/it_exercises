def wstawianie(tab):
    dl = len(tab)
    for i in range(1,dl):
        klucz = tab[i]
        j = i
        while j>0 and klucz<tab[j-1]:
            tab[j]=tab[j-1]
            j-=1
        tab[j] = klucz

def wydawanie(tab,nominaly,kwota):
    licznik = 0
    for i in range(len(nominaly)-1,-1,-1):
            while tab[i]>0 and kwota!=0:
                    if nominaly[i]>kwota:
                        break
                    tab[i] -= 1
                    kwota -= nominaly[i]
                    licznik += 1
    if kwota!=0:
        licznik = "Nie można wydać reszty"
    return licznik

tab=[0]*4
tablica_nominalow=[10,2,5,1]
wstawianie(tablica_nominalow)

for i in range(4):
    tab[i]=int(input())

kwota=int(input())

while kwota>100:
    kwota=int(input())

kwota = 100-kwota
print(wydawanie(tab,tablica_nominalow,kwota))
