def algorytm(P,n,m):
    A = []
    for i in range(n):
        wiersz = []
        for j in range(m):
            wiersz.append(False)
        A.append(wiersz)
    A[0][0] = True
    A[n - 1][m - 1] = True
    for i in range(n):
        for j in range(m):
            if P[i][j] == 0:
                A[i][j] = False
            else:
                if i == 0 and j != 0:
                    A[i][j] = A[i][j - 1]
                if i != 0 and j == 0:
                    A[i][j] = A[i - 1][j]
                if i != 0 and j != 0:
                    A[i][j] = A[i][j - 1] or A[i - 1][j]
    return A[n-1][m-1]




p1  = [[1,1,1],[0,1,0],[1,1,1]]
print(algorytm(p1,3,3))

P2  = [[1,1,1],[0,0,1],[1,1,1],[1,0,0],[0,0,0]]
print(algorytm(P2,5,3))

P3  = [[1,0,0,0,0],[1,1,0,0,1],[0,1,0,0,1],[0,1,1,1,0],[0,1,0,1,1]]
print(algorytm(P3,5,5))





