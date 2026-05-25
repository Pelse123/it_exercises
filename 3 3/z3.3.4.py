"""slowo = input()
n = len(slowo)
flaga = "jest palindromem"
for i in range(n//2):
    if slowo[i]!=slowo[n-i-1]:
        flaga = "nie jest palindromem"
        break
print(flaga)
"""
slowo = input()
n = len(slowo)
flaga = "jest palindromem"
i = 1
while i<=n//2:
    if slowo[i]!=slowo[n-i]:
        flaga = "nie jest palindromem"
        break
    i+=1
print(flaga)
