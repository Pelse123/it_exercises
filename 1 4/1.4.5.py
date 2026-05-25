def ile_razy_w_napisie(napis,litera):
    licznik =0
    if(ord(litera)<97):
        litera = chr(ord(litera)+32)
    for i in range(len(napis)):
        if napis[i] == litera or napis[i] == chr(ord(litera)-32):
            licznik += 1
    return licznik

tekst = input()
literka = input()
print(ile_razy_w_napisie(tekst,literka))