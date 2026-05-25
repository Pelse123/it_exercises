def funkcja(n):
    if n<=1:
        return False
    s = 1
    for i in range(2,(n//2)+1):
        if n%i==0:
            s = s+i
    if s==n:
        return True
    else:
        return False
print(funkcja(37))