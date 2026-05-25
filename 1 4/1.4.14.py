def usun_spacje(napis):
    nowy_napis=""
    for i in range(len(napis)):
        if napis[i]!=" ":
            nowy_napis += napis[i]
    return nowy_napis

napis = input()
print(usun_spacje(napis))