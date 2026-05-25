n = int(input())

if n == 0:
    w = 0
    print(w)
else:
    v = 0
    x = 1
    for i in range(1,n):
        w = x+v
        v=x
        x=w
    print(w)

"""
wczytaj n
jeżeli n = 0
    w<-0
    wypisz w
w przeciwnym wypadku
    v<-0
    x<-1
    dla i=1,2,3...,n wykonuj
        w <- x+v
        v<-x
        x<-w
    wypisz w   
"""