def przeksztalcenie_klucza(klucz):
    nowy_klucz = ""
    for i in range(len(klucz)):
        literka = klucz[i]
        if literka=='J':
            literka='I'
        if (literka in nowy_klucz)==False:
            nowy_klucz += literka
    return nowy_klucz

def przeksztalcenie_tekstu_jawnego(tekst):
    nowy_tekst=""
    index_litery_a_w_nowym_tekscie = 0
    for i in range(len(tekst)-1):
        literka_a = tekst[i]
        literka_b = tekst[i+1]
        if  index_litery_a_w_nowym_tekscie%2==0 and  literka_a == literka_b:
            nowy_tekst = nowy_tekst + literka_a + "X"
            index_litery_a_w_nowym_tekscie+=2
        else:
            nowy_tekst = nowy_tekst + literka_a
            index_litery_a_w_nowym_tekscie+=1
    nowy_tekst += tekst[len(tekst)-1]
    if len(nowy_tekst)%2==1:
        nowy_tekst += "X"
    return nowy_tekst

def tworzenie_macierzy(klucz):
    macierz = []
    for i in range(5):
        macierz.append([])
        for j in range(5):
            macierz[i].append(0)
    licznik_macierzy = 0
    for i in range(len(klucz)):
        macierz[licznik_macierzy//5][licznik_macierzy%5]=klucz[i]
        licznik_macierzy += 1
    for literka in range(ord('A'), ord('Z')+1):
        if chr(literka) == "J":
            continue
        if (chr(literka) in klucz) == False:
            macierz[licznik_macierzy // 5][licznik_macierzy % 5] = chr(literka)
            licznik_macierzy += 1
    return macierz

def znajdz_index_wiersza_kolumny(macierz,literka):
    for i in range(len(macierz)):
        for j in range(len(macierz)):
            if macierz[i][j]==literka:
                return i,j
    return -1


def szyfr_playfair(tekst,klucz):
    szyfrogram = ""
    nowy_klucz = przeksztalcenie_klucza(klucz)
    nowy_tekst = przeksztalcenie_tekstu_jawnego(tekst)
    macierz = tworzenie_macierzy(nowy_klucz)
    for i in range(0,len(nowy_tekst),2):
        literka_a = nowy_tekst[i]
        literka_b = nowy_tekst[i+1]
        index_wiersza_a,index_kolumny_a = znajdz_index_wiersza_kolumny(macierz,literka_a)
        index_wiersza_b,index_kolumny_b = znajdz_index_wiersza_kolumny(macierz,literka_b)
        if index_wiersza_a == index_wiersza_b:
            szyfrogram = szyfrogram + macierz[index_wiersza_a][(index_kolumny_a+1)%5]
            szyfrogram = szyfrogram + macierz[index_wiersza_b][(index_kolumny_b+1)%5]

        elif index_kolumny_a == index_kolumny_b:
            szyfrogram = szyfrogram + macierz[(index_wiersza_a + 1) % 5][index_kolumny_a]
            szyfrogram = szyfrogram + macierz[(index_wiersza_b + 1) % 5][index_kolumny_b]
        else:
            szyfrogram = szyfrogram + macierz[index_wiersza_a][index_kolumny_b]
            szyfrogram = szyfrogram + macierz[index_wiersza_b][index_kolumny_a]


    return szyfrogram

tekst = input()
klucz = input()
print(szyfr_playfair(tekst,klucz))
