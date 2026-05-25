def pierwsza(znak):
    liczba = int(znak)
    if liczba < 2:
        return False
    else:
        for i in range(2,liczba):
            if liczba % i == 0:
                return False
        return True
ciag = input()

odfiltrowany=list(map(lambda x: x , filter(lambda x: pierwsza(x) if x!=";" else False,ciag)))
print(odfiltrowany)
