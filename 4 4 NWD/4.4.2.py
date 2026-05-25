def nwd_re(a,b):
    if b == 0:
        return a
    return nwd_re(b,a%b)

n1 = int(input())
n2 = int(input())
print(nwd_re(n1,n2))
