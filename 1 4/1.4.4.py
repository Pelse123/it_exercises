def czy_palindrom(napis):
    palindrom = True
    for i in range(len(napis)):
        if napis[i]!=napis[len(napis)-1-i]:
            palindrom = False
    return palindrom


tekst = input()

if czy_palindrom(tekst):
    print("Podany napis jest palindromem")
else:
    print("Podany napis nie jest palindromem")