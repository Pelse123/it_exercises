def zadanie8_3(ciag):
    maks_dlugosc = 1
    dlugosc_ciagu = 1
    poczatek_ciagu = 0
    koniec_ciagu = 0
    for i in range(1,len(ciag)):
        if ciag[i-1]<ciag[i]:
            dlugosc_ciagu +=1
        else:
            if dlugosc_ciagu>maks_dlugosc:
                maks_dlugosc = dlugosc_ciagu
                poczatek_ciagu = i-maks_dlugosc
                koniec_ciagu = i
            dlugosc_ciagu = 1
    if dlugosc_ciagu > maks_dlugosc:
        maks_dlugosc = dlugosc_ciagu
        poczatek_ciagu = i - maks_dlugosc
        koniec_ciagu = i


    podciag = []
    for i in range(poczatek_ciagu,koniec_ciagu):
        podciag.append(ciag[i])
    return podciag

def rosnaco_malejacy(ciag):
    maks_dlugosc = 1
    dlugosc_ciagu = 1
    poczatek_ciagu = 0
    koniec_ciagu = 0
    czy_maleje = False
    for i in range(1, len(ciag)):
        if not czy_maleje:
            if ciag[i-1]<ciag[i]:
                dlugosc_ciagu += 1
            else:
                czy_maleje = True
                dlugosc_ciagu += 1
        else:
            if ciag[i - 1] > ciag[i]:
                dlugosc_ciagu += 1
            else:
                czy_maleje = False
                if dlugosc_ciagu > maks_dlugosc:
                    maks_dlugosc = dlugosc_ciagu
                    poczatek_ciagu = i - maks_dlugosc
                    koniec_ciagu = i
                dlugosc_ciagu = 1

    if dlugosc_ciagu > maks_dlugosc:
        maks_dlugosc = dlugosc_ciagu
        poczatek_ciagu = i - maks_dlugosc
        koniec_ciagu = i

    podciag = []
    for i in range(poczatek_ciagu,koniec_ciagu):
        podciag.append(ciag[i])
    return podciag

A = [5,7,9,12,10,8,6,4,11,13]
print(zadanie8_3(A))
print(rosnaco_malejacy(A))