def Rek(x,p,k,T):
    print(x,p,k)
    if p<k:
        s=(p+k)//2
        if T[s]>=x:
            return Rek(x,p,s,T)
        else:
            return Rek(x,s+1,k,T)
    else:
        if T[p]==x:
            return p
        else:
            return -1

T=[False,1,5,7,10,12,14,19,20,23,30,38]
print(Rek(7,1,11,T))
