def nwd_it(a,b):
    while b!=0:
        a,b = b,a%b
    return a

def nww(a,b,nwd):
    return a*b//nwd


n1 = int(input())
n2 = int(input())
nwd = nwd_it(n1,n2)
print(nww(n1,n2,nwd))
