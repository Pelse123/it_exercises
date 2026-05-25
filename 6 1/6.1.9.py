import math
def NWD(a,b):
    while b!=0:
        a,b = b,a%b
    return a
def NWW(a,b):
    return (a*b)/NWD(a,b)

liczba1 = int(input())
liczba2 = int(input())
print(math.lcm(liczba1,liczba2))
print(math.gcd(liczba1,liczba2))
print(NWD(liczba1,liczba2))
print(NWW(liczba1,liczba2))
