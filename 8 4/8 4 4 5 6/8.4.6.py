plik= open('mecz.txt', 'r')
zapis= open('wyniki1.txt', 'w')

linia = plik.readline().strip()

ilosc_passy = 0
najdluzsza_passa = 0
druzyna_ktora_osiagnela = ""
licznik_przebiegu_passy = 1

for i in range(1,len(linia)):
    if linia[i-1]==linia[i]:
        licznik_przebiegu_passy+=1
    else:
        if licznik_przebiegu_passy>=10:
            ilosc_passy+=1
            if licznik_przebiegu_passy>najdluzsza_passa:
                najdluzsza_passa=licznik_przebiegu_passy
                druzyna_ktora_osiagnela=linia[i-1]
        licznik_przebiegu_passy=1

zapis.write("c)\n")
zapis.write(f"Laczna liczba dobrych pass: {ilosc_passy}\nNajdluzsza dobra passa: {najdluzsza_passa}\nDruzyna ktora ja osiagnela: {druzyna_ktora_osiagnela}\n")


zapis.close()
plik.close()