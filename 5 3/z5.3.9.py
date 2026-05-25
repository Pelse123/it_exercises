def czy_palindrom(napis):
    for i in range(len(napis)//2):
        if napis[i] != napis[len(napis)-i-1]:
            return False
    return True

def znajdz_najdluzszy_palindrom(ciag):
    dlugosc=0
    index_od=0
    index_do=0
    for i in range(len(ciag)):
        slowo = ciag[i]
        for j in range(i+1,len(ciag)):
            slowo = slowo + ciag[j]
            if czy_palindrom(slowo):
                if dlugosc<len(slowo):
                    dlugosc = len(slowo)
                    index_od=i
                    index_do=j
    najdluzszy_palindrom = ""
    for i in range(index_od,index_do+1):
        najdluzszy_palindrom += ciag[i]
    return najdluzszy_palindrom


napis = input()
print(znajdz_najdluzszy_palindrom(napis))