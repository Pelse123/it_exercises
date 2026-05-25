a = int(input())
ilosc_a=0
b = int(input())
ilosc_b=0
while(True):
    if(a==0 and b==0):
        break
    if(a>0):
        ilosc_a = ilosc_a+1
    if(b>0):
        ilosc_b = ilosc_b+1
    a = a // 10
    b = b//10

if(ilosc_a==ilosc_b):
    print("Obie liczby mają tyle samo cyfr.")
elif(ilosc_a>ilosc_b):
    print("Pierwsza liczba ma więcej cyfr.")
else:
    print("Druga liczba ma więcej cyfr.")