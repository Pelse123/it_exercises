P=[
[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,1,1,1]
]
P[0][0]=True
n = len(P)
m = len(P[0])
for i in range(n):
    for j in range(m):
        if P[i][j]==0:
            P[i][j]=False
        else:
            if i==0 and j!=0:
                P[i][j]=P[i][j-1]
            if i!=0 and j==0:
                P[i][j]=P[i-1][j]
            if i!=0 and j!=0:
                P[i][j]=P[i][j-1] or P[i-1][j]

print(P[n-1][m-1])