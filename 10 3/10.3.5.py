d = int(input())
C = []
for i in range(d):
    C.append(int(input()))

w = 0
for i in range(d-1,-1,-1):
    w = w+C[i]*6**i
print(w)