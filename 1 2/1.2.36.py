a = int(input())
i=a
temp_a=0
ilosc_liczb = 0
while(i!=0):
    ilosc_liczb = ilosc_liczb + 1
    i = i//10
i = a
while(i!=0):
    modulo = i%10
    temp_a = temp_a+modulo**ilosc_liczb
    i = i//10

if temp_a == a:
    print("Tak")
else:
    print("Nie")
