"""def czy_pierwsza(n):
    for i in range(2,int(n**(1/2))+1):
        if n%i==0:
            return False
    return True
n = int(input())
while n<=1:
    n = int(input())
if czy_pierwsza(n):
    print("TAK")
else:
    print("NIE")"""

n = int(input())
flaga = False
for i in range(n):
    for k in range(n):
        if (i**2 + k**2) == n:
            print(i,k)
            flaga = True
            break
    if flaga:
        break


