a = int(input())
b = int(input())
c = int(input())
if(a+b>c and a+c>b and b+c>a):
    print("Podane liczby mogą być długościami boków trójkąta")
else:
    print("Podane liczby nie mogą być długościami boków trójkąta")