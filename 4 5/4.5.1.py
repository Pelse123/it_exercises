def szukaj(tekst,wzorzec):
    flaga = "Podany wzorzec nie znajduje sie w napisie"
    for i in range(len(tekst)-len(wzorzec)+1):
        ilosc_poprawnych_porownan = 0
        while ilosc_poprawnych_porownan<len(wzorzec)and tekst[i+ilosc_poprawnych_porownan]==wzorzec[ilosc_poprawnych_porownan]:
            ilosc_poprawnych_porownan+=1

        if ilosc_poprawnych_porownan==len(wzorzec):
            flaga = "Podany wzorzec znajduje sie w napisie"
    return flaga
tekst = input()
wzorzec = input()
print(szukaj(tekst,wzorzec))
