def push(stos,n):
    return stos.append(n)

def pop(stos):
    return stos.pop()

def peek(stos):
    return stos[len(stos)-1]

def isEmpty(stos):
    return len(stos)==0

nawiasy = input()
stos = []
glebokosc = 0
maks = 0
ostatni = ""
for i in range(len(nawiasy)):
    push(stos,nawiasy[i])

while isEmpty(stos)==False:
    if peek(stos)==")":
        glebokosc+=1
        if(glebokosc>maks):
            maks = glebokosc
    elif(peek(stos)=="("):
        glebokosc-=1
    pop(stos)

print(maks)

