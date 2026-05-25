class Moje_dzwieki():

    def __init__(self,artist:str,album:str,songsNumber:int,year:int,downloadNumber:int):
        self.artist = artist
        self.album = album
        self.songsNumber = int(songsNumber)
        self.year = int(year)
        self.downloadNumber = int(downloadNumber)

    def zwroc(self):
        return (f"{self.artist}\n{self.album}\n{self.songsNumber}\n{self.year}\n{self.downloadNumber}\n")


"""
**********************************************
nazwa funkcji: wczytaj_plik
opis funkcji: wczytuje plik do listy - plik_jako_tablica
parametry: brak
zwracany typ i opis: lista - plik_jako_tablica - lista zawiera każdą linijkę pliku Data.txt
autor: 694202137
***********************************************
"""
def wczytaj_plik():
    plik = open("Data.txt",encoding="utf-8")
    plik_jako_tablica = []
    for linia in plik:
        plik_jako_tablica.append(linia.strip())
    plik.close()
    return plik_jako_tablica
tablica_albumow = wczytaj_plik()
albumy = []
for i in range(0,len(tablica_albumow),6):
    album =Moje_dzwieki(tablica_albumow[i],tablica_albumow[i+1],tablica_albumow[i+2],tablica_albumow[i+3],tablica_albumow[i+4])
    albumy.append(album)
for i in range(len(albumy)):
    print(albumy[i].zwroc())


