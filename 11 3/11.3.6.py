#n=(n**2)%10**k gdzie k = len(str(n))

n = int(input())
k = 0
temp_n = n
while temp_n > 0:
    k+=1
    temp_n=temp_n//10

dziesiec_do_potegi = 10
i = 1
while i<k:
    dziesiec_do_potegi = dziesiec_do_potegi*10
    i+=1

wzor = (n*n)%dziesiec_do_potegi
if wzor==n:
    print("Tak")
else:
    print("Nie")