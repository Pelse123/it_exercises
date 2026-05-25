def czy_palindrom(linia):
    for i in range(len(linia)//2):
        if linia[i] != linia[len(linia)-1-i]:
            return False
    return True
plik = open("symbole_przyklad.txt","r")
for line in plik:
    if czy_palindrom(line.strip()):
        print(line.strip())

plik.close()