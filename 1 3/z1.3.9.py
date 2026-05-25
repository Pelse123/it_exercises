napis = input()
czypalindrom = True
for i in range(len(napis)//2):
    if napis[i]!=napis[len(napis)-1-i]:
        czypalindrom = False
        break
if czypalindrom:
    print("Podany napis jest palindromem")
else:
    print("Podany napis nie jest palindromem")