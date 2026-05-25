liczba_zer = 0
l = 0
p = 1023
A=[1]*1023
for i in range(321):
    A[i]=0

while l<=p:
    s = (l+p)//2
    if A[s]==1:
        p=s-1
    else:
        liczba_zer+=(s-l)+1
        l = s+1
print(l)
print(liczba_zer)
