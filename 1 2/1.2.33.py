a = int(input())
najwiekszydzielnik = 0
for i in range(2,a):
    if (a % i == 0):
        czypierwsza = True
        for j in range(2, i):
            if (i % j == 0):
                czypierwsza = False
                break
        if(czypierwsza):
            najwiekszydzielnik = i
if(najwiekszydzielnik > 0):
    print(najwiekszydzielnik)
else:
    print("Brak")







