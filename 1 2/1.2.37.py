n = int(input())
newton = 0
for i in range(n):
    newton = 1
    for j in range(i+1):
        print(newton,end=" ")
        newton = newton * (i - j) // (j + 1)
    print("")