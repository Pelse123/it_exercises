def push(stos,n):
    return stos.append(n)

def pop(stos):
    return stos.pop()

def peek(stos):
    return stos[len(stos)-1]

def isEmpty(stos):
    return len(stos)==0

def usun_backspace(stos):
    napis=""
    ilosc_usuniec = 0
    while not isEmpty(stos):
        if peek(stos)=="#":
            ilosc_usuniec+=1
            pop(stos)
        if peek(stos)!="#":
            if ilosc_usuniec>0:
                for i in range(ilosc_usuniec):
                    pop(stos)
                ilosc_usuniec = 0
            else:
                napis+=peek(stos)
                pop(stos)
    odwrocony_napis = ""
    for i in range(len(napis)):
        odwrocony_napis += napis[len(napis)-i-1]
    return odwrocony_napis

slowo = input()
drugie_slowo = input()
stos = []
drugi_stos=[]
for i in range(len(slowo)):
    push(stos,slowo[i])

slowo_do_sprawdzenia1 = usun_backspace(stos)

for i in range(len(drugie_slowo)):
    push(drugi_stos,drugie_slowo[i])
slowo_do_sprawdzenia2 = usun_backspace(drugi_stos)

if slowo_do_sprawdzenia1 == slowo_do_sprawdzenia2:
    print("Ciągi znaków są identyczne.")
else:
    print("Ciągi znaków nie są identyczne.")