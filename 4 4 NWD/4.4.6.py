def nwd(a,b):
    if b==0:
        return a
    return nwd(b,a%b)
n1 = int(input())
n2 = int(input())
if nwd(n1,n2) == 1:
    print("Liczby są względnie pierwsze")
else:
    print("Liczby nie są względnie pierwsze")

