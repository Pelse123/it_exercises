a,b,c = int(input()),int(input()),int(input())
maks = 0
if a>=b and a>=c:
    maks = a
elif b>=a and b>=c:
    maks = b
elif c>=a and c>=b:
    maks = c
print(maks)