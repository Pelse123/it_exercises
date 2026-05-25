def licz_wystapienia(slowo):
    slownik = {}
    for i in range(len(slowo)):
        ilosc = 0
        if slowo[i] != " ":
            for j in range(len(slowo)):
                if slowo[i] == slowo[j]:
                    ilosc = ilosc + 1
            slownik[slowo[i]] = ilosc
    return slownik

slowo = input()

slownik = licz_wystapienia(slowo)
for klucz in slownik:
    print(f"{klucz}: {slownik[klucz]}")

