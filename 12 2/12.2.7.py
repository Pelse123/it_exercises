n = int(input())
tm = 0
while n>0:
    o = n%10
    if o%2!=0:
        tm = tm*10+o
    n = n//10

if tm>0:
    m = 0
    while tm>0:
        m = m*10+tm%10
        tm = tm//10
    print(m)