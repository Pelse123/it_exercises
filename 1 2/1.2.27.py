a = int(input())
ilosc_a = a
i=0
while(ilosc_a>0):
    ilosc_a=ilosc_a//10
    i=i+1
ilosc = i

pierwsza_liczba = a%10
ostatnia_liczba = a//10**(ilosc-1)
a = (a%10**(ilosc-1))//10

liczba = pierwsza_liczba*10**(ilosc-1) +a*10 + ostatnia_liczba
print(liczba)

