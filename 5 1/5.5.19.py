def push(stos,n):
    stos.append(n)
def pop(stos):
    return stos.pop()
def czy_spacja(ciag,i):
    return ciag[i] == " "
def wykonaj_operacje(stos,dzialanie):
    stos1 = pop(stos)
    stos2 = pop(stos)
    wynik = 0
    if dzialanie == "+":
        wynik = stos2 + stos1
    elif dzialanie == "-":
        wynik = stos2 - stos1
    elif dzialanie == "*":
        wynik = stos2 *stos1
    elif dzialanie == "/":
        wynik = stos2 / stos1
    elif dzialanie == "^":
        wynik = stos2 ** stos1
    push(stos,wynik)
def operator(znak):
    return znak == "+" or znak == "-" or znak == "*" or znak == "/" or znak == "^"
def obliczenia_onp(ciag):
    stos = []
    warstwa= ""
    for i in range(len(ciag)):
        if operator(ciag[i]):
            if warstwa != "":
                push(stos,int(warstwa))
                warstwa = ""
            wykonaj_operacje(stos,ciag[i])
        elif czy_spacja(ciag,i):
            if warstwa != "":
                push(stos,int(warstwa))
                warstwa = ""
        else:
            warstwa = warstwa + ciag[i]

    if warstwa != "":
        push(stos,int(warstwa))
    return pop(stos)

ciag_onp = input()
print(obliczenia_onp(ciag_onp))
