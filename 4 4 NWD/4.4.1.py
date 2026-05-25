def nwd_it(a,b):
    while b!=0:
        a,b = b,a%b

    return a

n1 = int(input())
n2 = int(input())
print(nwd_it(n1,n2))
