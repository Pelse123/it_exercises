def czy_pierwsza(liczba):
    if isinstance(liczba,str):
        temp = ""
        for i in range(2,len(liczba)):
            temp += liczba[i]
        liczba = int(temp)
    if liczba<2:
        return False
    for i in range(2,int(liczba**0.5)+1):
        if liczba%i == 0:
            return False
    return True

liczba = int(input())
binarnie = bin(liczba)
if czy_pierwsza(liczba) and czy_pierwsza(binarnie):
    print(True)
else:
    print(False)
