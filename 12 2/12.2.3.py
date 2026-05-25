def czy_mniejszy(n,s,k1,k2):
    i = k1
    j = k2
    while i<=n and j<=n:
        if s[i]==s[j]:
            i=i+1
            j=j+1
        else:
            if (s[i]<s[j]):
                return True
            else:
                return False
    if j<=n:
        return True
    else:
        return False


plik1= open('pliki 12 2 3 4/slowa1.txt', 'r')
plik2= open('pliki 12 2 3 4/slowa2.txt', 'r')
plik3= open('pliki 12 2 3 4/slowa3.txt', 'r')
zapis= open('pliki 12 2 3 4/wyniki2_2.txt', 'w')

tablica1=[]
for linia in plik1:
    tablica1.append(linia.strip())
tablica2=[]
for linia in plik2:
    tablica2.append(linia.strip())
tablica3=[]
for linia in plik3:
    tablica3.append(linia.strip())

tablica1[2]=list(tablica1[2].split(" "))
tablica2[2]=list(tablica2[2].split(" "))
tablica3[2]=list(tablica3[2].split(" "))

tablica1[1]=" "+tablica1[1]
tablica2[1]=" "+tablica2[1]
tablica3[1]=" "+tablica3[1]

if (czy_mniejszy(int(tablica1[0]),tablica1[1],int(tablica1[2][0]),int(tablica1[2][1]))):
    zapis.write("TAK\n")
else:
    zapis.write("NIE\n")

if (czy_mniejszy(int(tablica2[0]),tablica2[1],int(tablica2[2][0]),int(tablica2[2][1]))):
    zapis.write("TAK\n")
else:
    zapis.write("NIE\n")

if (czy_mniejszy(int(tablica3[0]),tablica3[1],int(tablica3[2][0]),int(tablica3[2][1]))):
    zapis.write("TAK\n")
else:
    zapis.write("NIE\n")


zapis.close()
plik1.close()
plik2.close()
plik3.close()