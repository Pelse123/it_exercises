napis = input()
spacja = " "
napiszespacjami = ""
for i in range(len(napis)):
    napiszespacjami = napiszespacjami + napis[i]
    if napis[i] == spacja or i == len(napis)-1:
        print(napiszespacjami)
        napiszespacjami = ""
