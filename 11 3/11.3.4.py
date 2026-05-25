def sym(a,b,tablica):
    if a!=0:
        sym(a-1,b+1,tablica)
        tablica.append(a*b)
        sym(a-1,b+1,tablica)

tablica = []
sym(10,2020,tablica)
print(tablica)
print(len(tablica))