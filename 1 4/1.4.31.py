def power3(x,n):
    if n < 1:
        return 1
    if n%2 == 0:
        return power3(x,n//2)**2
    else:
        return x*power3(x,n//2)**2

x = int(input())
n = int(input())
while n < 0:
    n = int(input())
print(power3(x,n))