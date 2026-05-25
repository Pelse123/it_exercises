import math
p = int(input())
q = int(input())
while q<p:
    q=int(input())

roznica = p/q

while p!=0 and q!=0:
    a = math.ceil(q/p)
    if a==1:
        a +=1
    p1 = 1
    pom = q
    p = p*a
    q = q*a
    p1 = pom*p1
    p2 = a*pom
    p = p-p1
    print(a,end=" ")