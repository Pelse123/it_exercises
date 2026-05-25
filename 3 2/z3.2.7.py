x  = 1634
n = len(str(x))
k = x
suma = 0
while k>0:
    cyfra = k%10
    suma+=cyfra**n
    k = k//10
if suma == x:
    print("Prawda")
else:
    print("Fałsz")
