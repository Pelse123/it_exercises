def zamien_znak(znak):
    if znak>="A":
        return ord(znak)-55
    else:
        return int(znak)

def system_na_decymalny(s,n):
    decymalny = 0
    potega = 0
    dlugosc = len(n)
    for i in range(dlugosc-1,-1,-1):
        decymalny = decymalny + zamien_znak(n[i])*s**potega
        potega +=1
    return decymalny

s = int(input())
n = input()
print(system_na_decymalny(s,n))