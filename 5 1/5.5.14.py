def oblicz_pierwiastek_iteracyjnie(n,e):
    a = n/2
    b = n/a
    while abs(a-b) > e:
        a = (a+b)/2
        b = n / a
    return a

def oblicz_pierwiastek_rekurencyjnie(a,b,n,e):
    if abs(a-b) <= e:
        return a
    a = (a + b) / 2
    return oblicz_pierwiastek_rekurencyjnie(a,n/a,n,e)

n = float(input())
e = float(input())
a = n/2
b = n/a

print(oblicz_pierwiastek_rekurencyjnie(a,b,n,e))