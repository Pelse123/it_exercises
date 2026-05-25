a = int(input())
b = int(input())
while(a>b):
    a = int(input())
    b = int(input())
for i in range(a,b+1):
    if((i%5==0) and (i%10!=0)):
        print(i)