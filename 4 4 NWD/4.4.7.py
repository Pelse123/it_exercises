def nwd(a,b):
    if b==0:
        return a
    return nwd(b,a%b)

a = int(input())
b = int(input())
for i in range(1,a+1):
    czy_wzglednie = nwd(i,b)
    if czy_wzglednie == 1:
        print(i,end=" ")

