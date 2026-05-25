def suma_cyfr(n):
    s = 0
    temp_n=n
    while temp_n>0:
        s += temp_n%10
        temp_n //= 10
    return s
#suma n + (k*9) == n
n = int(input())
l = 0
r = n
k = n//2
while suma_cyfr(n) + (k*9)!=n:
    wzor = suma_cyfr(n) + (k*9)
    if wzor>n:
        r = k
        k = ((r+l)+1)//2
        wzor = suma_cyfr(n) + (k * 9)
    else:
        l = k
        k = ((r+l)+1)//2
        wzor = suma_cyfr(n) + (k * 9)
print(k)

