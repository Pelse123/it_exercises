
"""
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

print(przestaw(998877665544321,0))

"""

def przestaw2(n):
    w = 0
    c = 0
    while n>0:
        r = n%100
        a = r//10
        b = r%10
        if n//100 != 0:
            c = (b + 10 * a)+c*100
        else:
            c = c*10+n
        n = n//100

    while c > 0:
        w = (c % 10) + (w * 10)
        c = c // 10

    return w
print(przestaw2(998877665544321))


