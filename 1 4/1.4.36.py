def schodki(n):
    if n<0:
        return 0
    if n==0:
        return 1
    return schodki(n-1) + schodki(n-2)

n = int(input())
print(schodki(n))
