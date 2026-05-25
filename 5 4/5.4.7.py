def oblicz_hanoi_rekurencyjnie(a,b,c,krazki):
    if krazki == 0:
        return ""
    L = oblicz_hanoi_rekurencyjnie(a,c,b,krazki-1)
    P = oblicz_hanoi_rekurencyjnie(b,a,c,krazki-1)
    return L+a+c+P

a=input()
b=input()
c=input()
krazki = int(input())
print(oblicz_hanoi_rekurencyjnie(a,b,c,krazki))