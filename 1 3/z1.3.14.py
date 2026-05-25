napis = input()
bezpowtorzen = ""

for i in range(len(napis)):
    czyjest = True
    for j in range(len(bezpowtorzen)):
        if(napis[i]==bezpowtorzen[j]):
            czyjest = False
    if(czyjest):
        bezpowtorzen = bezpowtorzen + napis[i]

print(bezpowtorzen)

