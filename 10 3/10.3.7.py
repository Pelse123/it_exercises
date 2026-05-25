s = input()
n = len(s)
ile = 0
k = 0
r=""
for i in range(n-1,-1,-1):
    r = r+ s[i]
    k=k+1

for i in range(n):
    if r[i]==s[i]:
        ile = ile+1
    else:
        break

p = [""]*n
print(ile)
if ile==n:
    ile = ile//2

for i in range(ile):
    p[i] = s[i]
    p[i+ile]=s[n+i-ile]

print(n)
print(s)
print(ile)
print(p)
