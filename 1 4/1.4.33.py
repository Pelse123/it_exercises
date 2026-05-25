def rozbij_na_czynniki(n,dzielnik):
    if n == 1 :
        return 1
    if n%dzielnik==0:
        print(dzielnik)
        return rozbij_na_czynniki(n//dzielnik,dzielnik)
    return rozbij_na_czynniki(n,dzielnik+1)

n = int(input())
rozbij_na_czynniki(n,2)


"""n = 84
dzielnik = 2
while n > 0:
    if n%dzielnik == 0:
        print(dzielnik)
        n = n//dzielnik
    else:
        dzielnik +=1
"""