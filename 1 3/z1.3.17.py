napis = input()
spacja = " "
napiszespacjami = ""
for i in range(len(napis)):
    if napis[i-1] == spacja or i==0 :
        if(ord(napis[i])<92):
            napiszespacjami = napiszespacjami + napis[i]
        else:
            napiszespacjami = napiszespacjami + chr(ord(napis[i])-32)
    else:
        napiszespacjami = napiszespacjami + napis[i]
print(napiszespacjami)