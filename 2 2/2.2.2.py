def push(stos,n):
    return stos.append(n)

def pop(stos):
    return stos.pop()

def peek(stos):
    return stos[len(stos)-1]

def isEmpty(stos):
    return len(stos)==0

zdanie = input()
stos = []
slowo = ""
for i in range(len(zdanie)):
    if zdanie[i] != " ":
        slowo += zdanie[i]
    else:
        push(stos, slowo)
        slowo = ""
    if i == len(zdanie)-1:
        push(stos, slowo)

while isEmpty(stos)==False:
    wyswietl = peek(stos)
    print(wyswietl,end=" ")
    pop(stos)