def analizaSprzetu(slownik):
    unikalne = []
    klucze = []
    for klucz in slownik:
        wartosc = slownik[klucz]
        klucze.append(klucz)
        unikalne.append(wartosc)
    nowy_slownik = {
        klucze[0]:unikalne[0]-unikalne[1]-unikalne[2],
        klucze[1]:unikalne[1]-unikalne[2]-unikalne[0],
        klucze[2]:unikalne[2]-unikalne[0]-unikalne[1],
    }
    return nowy_slownik

biura = {
    "Biuro1": {"komputer", "drukarka", "skaner", "projektor"},
    "Biuro2": {"komputer", "drukarka", "telewizor"},
    "Biuro3": {"komputer", "drukarka", "projektor", "telefon"}
}
slownik = analizaSprzetu(biura)
for klucz in slownik:
    wartosc = slownik[klucz]
    print(f"{klucz}: {wartosc}")
