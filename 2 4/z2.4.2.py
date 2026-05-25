slowo1 = input()
slowo2 = input()
slowo1 = set(slowo1)
slowo2 = set(slowo2)
unikalne1 = slowo1 - slowo2
unikalne2 = slowo2 - slowo1

for i in unikalne1:
    print(i,end=" ")
print()
for i in unikalne2:
    print(i,end=" ")