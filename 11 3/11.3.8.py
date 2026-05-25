def modyfikuj(s,k,T,n):
    print(1)
    if s+k<n:
        modyfikuj(s+k,k,T,n)
    i = s+1
    while i<=n and i<=s+k:
        T[s] = T[s]+T[i]
        i = i+1
T = [False,1,1,1,1,1,1,1,1]
n = len(T)-1
modyfikuj(3,3,T,n)
print(T)