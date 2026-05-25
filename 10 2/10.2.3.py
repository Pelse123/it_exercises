def zamien_na_2(s):
    l = 0
    while s>0:
        if s%2 == 1:
            l +=1
        s=s//2
    return l
s = int(input())
l = zamien_na_2(s)
print(l)
