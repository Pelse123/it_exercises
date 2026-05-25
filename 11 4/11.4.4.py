n = int(input())
w = 0
temp_n = n
for i in range(1,n+1):
    w = w+temp_n*i
    temp_n -=1
print(w)