def czy_w_przedziale_13_19(a,b,c):
    return (a >= 13 and a <= 19) or (b >= 13 and b <= 19) or (c >= 13 and c <= 19)

a=int(input())
b=int(input())
c=int(input())

if(czy_w_przedziale_13_19(a,b,c)):
    print("Co najmniej jedna z tych liczb jest w przedziale 13-19")
else:
    print("Zadna z tych liczb nie jest w przedziale 13-19")