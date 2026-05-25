n =int(input())

X=[0]*(n+1)
Y=[0]*(n+1)

for i in range(1,n+1):
    X[i]=int(input())
for i in range(1,n+1):
    Y[i]=int(input())

R=[0]*(n+1)
i = 1
while i<=n:
    R[i]=X[i]/Y[i]
    i+=1

i = 1
while i<n+1:
    j = 1
    while j<n+1-i:
        if R[j]>R[j+1]:
            pomX=X[j]
            pomY=Y[j]
            X[j]=X[j+1]
            Y[j]=Y[j+1]
            X[j+1]=pomX
            Y[j+1]=pomY
        j+=1
    i+=1

i = 1
while i<n+1:
    print(X[i],Y[i])
    i+=1
