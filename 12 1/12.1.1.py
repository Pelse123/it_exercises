n = int(input())
p = 1
q = n
while p<q:
    s = (p+q)//2
    print(p,s,q)
    if s*s*s <n:
        p = s+1
    else:
        q = s
print(p)