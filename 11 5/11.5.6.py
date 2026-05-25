n = int(input())
P=[]
S=[]
for i in range(n+1):
   P.append(1)
   S.append(0)
P[0]=False
S[0]=False
for j in range(2,n+1):
    if P[j]==1:
        i = j*j
        while i<=n:
            P[i]=0
            i=i+j
    S[j]=S[j-1]+P[j]
print(P)
print(S)