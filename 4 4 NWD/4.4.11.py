
def doskonala(l):
    dzielniki = 0
    for i in range(1,(l//2)+1):
        if l%i==0:
            dzielniki = dzielniki+i
    return dzielniki == l

a = int(input())
b = int(input())
for i in range(a,b+1):
    if doskonala(i):
        print(i,end=" ")


