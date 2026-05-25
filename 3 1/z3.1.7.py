def sn(n,k):
    if k==0 or k==n:
        return 1
    else:
        return sn(n-1,k-1)+sn(n-1,k)

print(sn(3,0))