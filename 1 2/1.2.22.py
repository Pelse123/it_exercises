a = int(input())
lparzystych = 0
lnieparzystych = 0
while(a!=0):
    print(a)
    if(a%2==0):
        lparzystych += 1
    else:
        lnieparzystych += 1
    a = a//10
if(lparzystych==lnieparzystych):
    print("Liczba zawiera tyle samo cyfr parzystych, co nieparzystych")
elif(lnieparzystych>lparzystych):
    print("Liczba zawiera więcej cyfr nieparzystych")
else:
    print("Liczba zawiera więcej cyfr parzystych")