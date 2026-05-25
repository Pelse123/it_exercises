def przestaw(n,l):
    l = l+1
    print("wywolana:",l)
    r = n%100
    a = r//10
    b = r%10
    n = n//100
    if n>0:
        w = a+10*b+100*przestaw(n,l)
    else:
        if a>0:
            w = a+10*b
        else:
            w = b

    return w

print(przestaw(2143,0))