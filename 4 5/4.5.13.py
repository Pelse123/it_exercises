def wstawianie(napis):
    tablica = list(napis)
    for i in range(1,len(tablica)):
        klucz = tablica[i]
        j = i
        while j>0 and tablica[j-1]>klucz:
            tablica[j],tablica[j-1] = tablica[j-1],tablica[j]
            j-=1
        tablica[j] = klucz
    return tablica

n1=input()
n2=input()
if wstawianie(n1) == wstawianie(n2):
    print("TAK")
else:
    print("NIE")