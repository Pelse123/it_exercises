
tablica = []
ile = int(input())
for i in range(ile):
    tablica.append(input())

for i in range(ile):
    czypalindrom = True
    napis = tablica[i]
    for j in range(len(napis)//2):
        if(napis[j]!=napis[len(napis)-1-j]):
            czypalindrom = False
            break
    if(czypalindrom):
        print(napis)



