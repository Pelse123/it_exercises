def push(stos,n):
    return stos.append(n)

def pop(stos):
    return stos.pop()

def peek(stos):
    return stos[len(stos)-1]

def isEmpty(stos):
    return len(stos)==0

ile_wartosci = int(input())
stos = []
maks = 0

for i in range(ile_wartosci):
    liczba_w_stosie = int(input())
    push(stos,liczba_w_stosie)
    if liczba_w_stosie>maks:
        maks = liczba_w_stosie
print(maks)

