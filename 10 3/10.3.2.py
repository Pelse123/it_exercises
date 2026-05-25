a=[False,21,1,56,90,8,8,19,47]
i = 1
n = len(a)
while i<n:
    if a[i]>a[i+1]:
        a[i],a[i+1]=a[i+1],a[i]
    i+=2
print(a)
min = a[1]
max = a[2]
i = 3
while i<n:
    print(i)
    if a[i]<min:
        min = a[i]
    if a[i+1]>max:
        max = a[i+1]
    i=i+2
print(min)
print(max)