a = int(input())
floata = a**(1/2)
czypierwsza = True
if(a<2):
    czypierwsza = False
else:
    for i in range(2,int(floata)):
        if(a%i==0):
            czypierwsza = False
            break

if(czypierwsza == True):
    print("Ta liczba jest pierwsza")
else:
    print("Ta liczba nie jest pierwsza")



