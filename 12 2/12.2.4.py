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


plik= open('pliki 12 2 3 4/slowa4.txt', 'r')
zapis= open('pliki 12 2 3 4/wyniki2_4.txt', 'w')

tablica = []
for linia in plik:
    tablica.append(linia.strip().split(" "))


tablica_od=[]
for i in range(len(tablica)):
    n = int(tablica[i][0])
    s = tablica[i][1]
    s = " "+s
    T=[0]*(n+1)
    i = 1
    while i<=n:
        T[i]=i
        i=i+1
    i = 0
    while i<n:
        j=1
        while j<n-i:
            k1 = T[j]
            k2 = T[j+1]
            if czy_mniejszy(n,s,k1,k2)==False:
                pom = T[j+1]
                T[j+1]=T[j]
                T[j]=pom
            j=j+1
        i=i+1
    tablica_od.append(T[1])
for i in range(len(tablica)):
    slowo = ""
    for j in range(tablica_od[i]-1,len(tablica[i][1])):
        slowo += tablica[i][1][j]
    zapis.write(slowo)
    zapis.write("\n")
zapis.close()
plik.close()