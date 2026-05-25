def F(x):
    if x==0:
        return 0
    else:
        return 2+ F(x//2)

print(2**8)
print(F(511))