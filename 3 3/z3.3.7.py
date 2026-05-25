n = int(input())
i = 2
while i <= n:
    j = 2
    while j * j <= i:
        if i % j == 0:
            break
        else:
            j = j + 1
    else:
        print(i)
    i = i + 1