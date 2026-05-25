def fun(a,b):
    if a<=2:
        if a==2:
            return True
        else:
            return False
    if a%b == 0:
        return False
    if b*b>a:
        return True
    print("wywolano")
    return fun(a,b+1)

print(fun(77,2))