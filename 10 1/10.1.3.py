
n = int(input())
tablica = [""]*n
while n<1:
    n = int(input())
S = input()
i = 0
while i<n:
    tablica[i] = S[i]
    i=i+1
if n%2==0:
    i = 1
    while i<n:
        tablica[i],tablica[i-1] = tablica[i-1],tablica[i]
        i+=2
else:
    tablica[0],tablica[n-1]=tablica[n-1],tablica[0]
    i = 1
    while i < n:
        tablica[i],tablica[i-1] = tablica[i-1],tablica[i]
        i += 2
S=""
i = 0
while i<n:
   S+=tablica[i]
   i+=1
print(S)