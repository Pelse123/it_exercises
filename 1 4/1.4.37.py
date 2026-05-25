def catalan(n):
    if n == 0:
        return 1
    zwroc = 0
    for i in range(n):
        zwroc = zwroc + catalan(i) * catalan(n - 1 - i)
    return zwroc
n = int(input())
print(catalan(n))