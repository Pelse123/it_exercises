print("-------------------------------------------------------")
print("Menu, wybierz figurę wpisując cyfrę obok figury.")
print("1.Kwadrat")
print("2.Prostokąt")
print("3.Trójkąt")
print("4.Trapez")
print("5.Równoległobok")
print("6.Sześcian")
print("7.Prostopadłościan")
print("8.Walec")
print("-------------------------------------------------------")
figura = int(input())
if figura == 1:
    a = int(input("Podaj a: "))
    wzor = a**2
    print(f"Twój kwadrat ma pole o rozmiarze: {wzor}")
elif figura == 2:
    a = int(input("Podaj a: "))
    b = int(input("Podaj b: "))
    wzor = a*b
    print(f"Twój prostokąt ma pole o rozmiarze: {wzor}")
elif figura == 3:
    a = int(input("Podaj a: "))
    h = int(input("Podaj h: "))
    wzor = (a*h)/2
    print(f"Twój trójkąt ma pole o rozmiarze: {wzor}")
elif figura == 4:
    a = int(input("Podaj a: "))
    b = int(input("Podaj b: "))
    h = int(input("Podaj h: "))
    wzor = ((a+b)*h)/2
    print(f"Twój trapez ma pole o rozmiarze: {wzor}")
elif figura == 5:
    a = int(input("Podaj a: "))
    h = int(input("Podaj h: "))
    wzor = a*h
    print(f"Twój równoległobok ma pole o rozmiarze: {wzor}")
elif figura == 6:
    a = int(input("Podaj a: "))
    v = a**3
    print(f"Twój sześcian ma objętość o rozmiarze: {v}")
elif figura == 7:
    a = int(input("Podaj a: "))
    b = int(input("Podaj b: "))
    c = int(input("Podaj c: "))
    v = a*b*c
    print(f"Twój prostopadłościan ma objętość o rozmiarze: {v}")
elif figura == 8:
    r = int(input("Podaj r: "))
    h = int(input("Podaj h: "))
    pi = 3.14
    v = pi*(r**2)*h
    print(f"Twój prostopadłościan ma objętość o rozmiarze: {v}")
else:
    print(f"Podano złą wartość: {figura} wybierz od 1 do 8")