a = int(input())

for i in range(2,a+1):
    while(a%i==0):
        a = a/i
        print(i)
        if(a==1):
            break