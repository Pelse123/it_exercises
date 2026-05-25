
class Album:
    ilosc = 0
    def __init__(self,artists,album,songsNumber,year,downloadNumber):
        self.artists = str(artists)
        self.album = str(album)
        self.songsNumber = int(songsNumber)
        self.year = int(year)
        self.downloadNumber = int(downloadNumber)
        Album.ilosc += 1

    def __str__(self):
        return f"{self.artists}\n{self.album}\n{self.songsNumber}\n{self.year}\n{self.downloadNumber}"

def pobierz_dane():
    plik = open("Data.txt","r",encoding="utf-8")
    tablica=[]
    for linie in plik:
        tablica.append(linie.strip().replace("\ufeff", ""))
    plik.close()
    return tablica

def dodaj_dane(tablica):
    albumy = []
    for i in range(0,len(tablica),6):
        obiekt = Album(tablica[i],tablica[i+1],tablica[i+2],tablica[i+3],tablica[i+4])
        albumy.append(obiekt)
    return albumy

def wyswietl(tablica):
    for i in range(0,len(tablica)):
        print(tablica[i])
        if(i!=len(tablica)-1):
            print()

def wyswietl_pojedynczy(tablica,nr):
    print()
    print(tablica[nr-1])

klasa = dodaj_dane(pobierz_dane())
wyswietl(klasa)
wyswietl_pojedynczy(klasa,7)
print()
print(Album.ilosc)

