"""s="eiindaezotinwezssyktpo"
d = len(s)
szyfr=""
k=2
n=2
for j in range(0,d):
    szyfr+=s[j]
i = 0
szyfr = list(szyfr)
while i < d-k:
    print(i,i+n)
    szyfr[i],szyfr[i+k]=szyfr[i+k],szyfr[i]
    i=i+n
print(szyfr)"""

s=input()
d = len(s)
szyfr=""
k=int(input())
n=int(input())
for j in range(0,d):
    szyfr+=s[j]
i = 1
szyfr = list(szyfr)
while i+n < d-k:
    i = i+n
while i>=1:
    print(i,i+k)
    szyfr[i],szyfr[i+k]=szyfr[i+k],szyfr[i]
    i=i-n
print(szyfr)