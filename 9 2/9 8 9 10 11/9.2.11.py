plik = open('dane8.txt', 'r')
zapis = open('wyniki8.txt', 'w')

tablica = []
for linia in plik:
    tablica.append(int(linia.strip()))

tablica_ciagow = [1]*len(tablica)

for i in range(len(tablica)):
    for j in range(i):
        if tablica[i]>tablica[j] and tablica_ciagow[i]<tablica_ciagow[j]+1:
            tablica_ciagow[i] = tablica_ciagow[j]+1

dlugosc = max(tablica_ciagow)
zapis.write(f"{dlugosc}\n")


zapis.close()
plik.close()