
n = int(input())
dl = 0
i = n
while i > 0:
    while i*i<=n:
        n = n - i*i
        dl = dl + 1
        if n == 0:
            break
    if n == 0:
        break
    i=i-1
print(dl)

