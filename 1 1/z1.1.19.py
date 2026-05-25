z1 = int(input())*1
z2 = int(input())*3
z3 = int(input())*7
z4 = int(input())*9
z5 = int(input())*1
z6 = int(input())*3
z7 = int(input())*7
z8 = int(input())*9
z9 = int(input())*1
z10 = int(input())*3
z11 = int(input())*1

suma = z1+z2+z3+z4+z5+z6+z7+z8+z9+z10+z11
if(suma%10==0):
    print("Podany PESEL jest poprawny")
else:
    print("Podany PESEL nie jest poprawny")
