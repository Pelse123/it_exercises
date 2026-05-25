def czy_mniejszy(n,s,k1,k2):
    i = k1
    j = k2
    while i<=n and j<=n:
        if s[i]==s[j]:
            i=i+1
            j=j+1
        else:
            if (s[i]<s[j]):
                return True
            else:
                return False
    if j<=n:
        return True
    else:
        return False

n = int(input())
s = input()
s = " "+s
T=[0]*(n+1)
i = 1
while i<=n:
    T[i]=i
    i=i+1
i = 0
while i<n:
    j=1
    while j<n-i:
        k1 = T[j]
        k2 = T[j+1]
        if czy_mniejszy(n,s,k1,k2)==False:
            pom = T[j+1]
            T[j+1]=T[j]
            T[j]=pom
        j=j+1
    i=i+1

print(T)