def iloczyn(x,y):
    if y == 1:
        return x
    else:
        k = y//2
        z = iloczyn(x,k)
        if y%2==0:
            return z+z

        else:
            return x+z+z

def iloczyn_i(x,y):
    z = 0
    while y>=1:
        if y%2==1:
            z=z+x
        x=x+x
        y=y//2
    return z


print(iloczyn(112,112))
print(iloczyn_i(112,112))