def szukaj(tekst,wzorzec):
    ile_wzorcow=0
    for i in range(len(tekst)-len(wzorzec)+1):
        ilosc_poprawnych_porownan = 0
        while ilosc_poprawnych_porownan<len(wzorzec)and tekst[i+ilosc_poprawnych_porownan]==wzorzec[ilosc_poprawnych_porownan]:
            ilosc_poprawnych_porownan+=1
        if ilosc_poprawnych_porownan==len(wzorzec):
            ile_wzorcow+=1
    return(ile_wzorcow)
tekst = input()
wzorzec = input()
print(szukaj(tekst,wzorzec))
