def wykonaj_potegowanie_modularne(a,b,m):
    if b==0:
        return 1
    if b%2==0:
        return wykonaj_potegowanie_modularne((a*a)%m,b//2,m)
    else:
        return (a%m)*wykonaj_potegowanie_modularne(a,b-1,m)%m
a = int(input())
b = int(input())
m = int(input())
print(wykonaj_potegowanie_modularne(a,b,m))