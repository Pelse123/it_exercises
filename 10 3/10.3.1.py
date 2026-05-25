d = 1
n =int(input())
iloczyn = 1
while d < n:
    if n % d==0:
        if d<n:
            iloczyn = iloczyn * d
    d+=1
if iloczyn == n:
    print("TAK")
else:
    print("NIE")
