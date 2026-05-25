
def wykonaj_potegowanie_szybkie_rekurencyjnie(a,b):
    if b==0:
        return 1
    if b%2==0:
        return (wykonaj_potegowanie_szybkie_rekurencyjnie(a*a,b//2))
    else:
        return (a*wykonaj_potegowanie_szybkie_rekurencyjnie(a,b-1))

a = int(input())
b = int(input())
print(wykonaj_potegowanie_szybkie_rekurencyjnie(a,b))
