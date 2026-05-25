def wydawanie(tab,kwota):
    min_ilosc=0
    for i in range(len(tab)):
        while kwota>=tab[i]:
            min_ilosc+=1
            kwota-=tab[i]
    return min_ilosc

def sortowanie(tab):
    for i in range(len(tab)):
        min_index = i
        for j in range(i+1,len(tab)):
            if tab[min_index] < tab[j]:
                min_index = j
        tab[i], tab[min_index] = tab[min_index], tab[i]


n = int(input())
tablica_monet=[]
for i in range(n):
    tablica_monet.append(int(input()))
sortowanie(tablica_monet)
kwota_do_wydania = int(input())
print(wydawanie(tablica_monet,kwota_do_wydania))