a = int(input())
modulo = 0
najwieksza = 0
najmniejsza = a
while(a!=0):
    modulo = a%10
    if(modulo>najwieksza):
        najwieksza = modulo
    if(modulo<najmniejsza):
        najmniejsza = modulo
    a = a//10
print(najwieksza)
print(najmniejsza)