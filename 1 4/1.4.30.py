def power2(x,n):
    if n == 0:
        return 1
    return x*power2(x,n-1)

x = int(input())
n = int(input())
while n < 0:
    n = int(input())
print(power2(x,n))