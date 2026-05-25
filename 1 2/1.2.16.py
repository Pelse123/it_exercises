a = int(input())
b = int(input())
while(a>b):
    a = int(input())
    b = int(input())
i = a
while(i<=b):
    if(i%5==0) and (i%10!=0):
        print(i)
    i=i+1
