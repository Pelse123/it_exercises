def power1(x,n):
    potega = 1
    for i in range(n):
        potega = potega*x
    return potega


x = int(input())
n = int(input())
while n < 0:
    n = int(input())

print(power1(x,n))