def oblicz_pierwiastek_szescienny(n,e):
    a = n / 3
    b = (2 * a + n / (a * a)) / 3
    while abs(a - b) > e:
        a = b
        b = (2 * a + n / (a * a)) / 3
    return b


n = float(input())
e = float(input())
print(oblicz_pierwiastek_szescienny(n, e))
