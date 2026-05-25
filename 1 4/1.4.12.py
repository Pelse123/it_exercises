def odleglosc_miedzy_punktami(x1,y1,x2,y2):
    odleglosc = (((x2-x1)**2)+((y2-y1)**2))**(1/2)
    return odleglosc
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(odleglosc_miedzy_punktami(x1, y1, x2, y2))