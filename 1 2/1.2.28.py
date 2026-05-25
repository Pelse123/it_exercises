a = int(input())
temp_a = a
odwrocona = 0
while(temp_a!=0):
    modulo = temp_a%10
    odwrocona = odwrocona*10+modulo
    temp_a=temp_a//10
if(odwrocona==a):
    print("Liczba jest palindromiczna")
else:
    print("Liczba nie jest palindromiczna")