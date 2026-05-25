slowo = input()
n = len(slowo)
flaga = "jest palindromem"
for i in range(n//2):
    if slowo[i]!=slowo[n-i-1]:
        flaga = "nie jest palindromem"
        break
print(flaga)

"""
1. przypisz zmiennej flaga napis "jest palindromem"
2.dla i od 1,...n//2:
    2.1 Jeżeli slowo[i] != slowo[n-i-1]; przypisz zmiennej flaga napis "nie jest palindromem" i zakończ obrót pętli
3. wypisz zmienną flaga
"""