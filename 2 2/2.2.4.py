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

czy_poprawny = "jest poprawne."

for i in range(len(nawiasy)):
    if nawiasy[i] == "(" or nawiasy[i] == "{" or nawiasy[i] == "[":
        push(stos,nawiasy[i])
    elif nawiasy[i] == ")" or nawiasy[i] == "]" or nawiasy[i] == "}":
        if isEmpty(stos):
            czy_poprawny = "jest niepoprawne."
            break
        if ((nawiasy[i] == ")" and peek(stos)!="(") or (nawiasy[i] == "}" and peek(stos)!="{") or (nawiasy[i] == "]" and peek(stos)!="[")):
            czy_poprawny = "jest niepoprawne."
            break
        pop(stos)

if isEmpty(stos) == False:
    czy_poprawny = "jest niepoprawne."

print(f'"{nawiasy}" - {czy_poprawny}')





