
n =int(input())

X=[0]*(n+1)
Y=[0]*(n+1)

for i in range(1,n+1):
    X[i]=int(input())
for i in range(1,n+1):
    Y[i]=int(input())

mini_roznica = X[1]/Y[1]
mini_x = X[1]
mini_y = Y[1]
for i in range(2,n):
    roznica = X[i]/Y[i]
    if roznica < mini_roznica:
        roznica = mini_roznica
        mini_x = X[i]
        mini_y = Y[i]

print(mini_x)
print(mini_y)

