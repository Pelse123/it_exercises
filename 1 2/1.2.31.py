a = int(input())
iloscpierwszych = 0
while(a != 0):
    czypierwsza = True
    modulo = a % 10
    if (modulo < 2):
        czypierwsza = False
    else:
        for i in range(2, modulo):
            if (modulo % i == 0):
                czypierwsza = False
                break
    if(czypierwsza):
        iloscpierwszych = iloscpierwszych +1
    a = a//10
print(iloscpierwszych)