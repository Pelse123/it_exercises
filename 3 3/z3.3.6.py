n = int(input())
suma = 0
i = 1
while i <= n:
    if i %3 ==0 or i %5 ==0:
        suma += i
    i=i+1
print(suma)