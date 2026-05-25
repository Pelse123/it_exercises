a = int(input())
czypierwsza = True
if(a<2):
    czypierwsza = False
else:
    for i in range(2,a):
        if(a%i==0):
            czypierwsza = False
            break

if(czypierwsza == True):
    print("Ta liczba jest pierwsza")
else:
    print("Ta liczba nie jest pierwsza")



