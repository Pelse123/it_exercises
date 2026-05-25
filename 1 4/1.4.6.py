def czy_poprawny_pesel(a):
    suma = 0
    tablicamnozenia = [1,3,7,9,1,3,7,9,1,3,1]
    for i in range(len(a)):
        suma += tablicamnozenia[i]*(ord(a[i])-48)
    return suma

pesel = input()

if(czy_poprawny_pesel(pesel)%10 == 0) and len(pesel)==11:
    print("Podany PESEL jest poprawny")
else:
    print("Podany PESEL nie jest poprawny")