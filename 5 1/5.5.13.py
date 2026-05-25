def oblicz_pierwiastek_iteracyjnie(n,e):
    a = n/2
    b = n/a
    while abs(a-b) > e:
        a = (a+b)/2
        b = n / a
    return a
n = float(input())
e = float(input())
print(oblicz_pierwiastek_iteracyjnie(n,e))