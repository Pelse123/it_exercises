a = int(input())
b = int(input())
k = int(input())
iloczyn = 1
while(a>b):
    a = int(input())
    b = int(input())
    k = int(input())
for i in range(a,b+1):
    if(i%k==0):
        iloczyn = i*iloczyn
print(iloczyn)