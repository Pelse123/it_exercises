T = [False,6,-4,12,27,26,8]
n = len(T)
s = n-1
while ((s//2)>=1) and (T[s]>T[s//2]):
    pom = T[s]
    T[s] = T[s//2]
    T[s//2] = pom
    s=s//2
print(T)
