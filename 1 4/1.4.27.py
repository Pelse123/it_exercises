def silnia_rekurencyjnie(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return silnia_rekurencyjnie(n-1)*n
n = int(input())
print(silnia_rekurencyjnie(n))