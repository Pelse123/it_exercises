def zlicz_znaki(slowo):
    alfabet = [0]*26
    for i in range(len(slowo)):
        alfabet[ord(slowo[i])-ord("a")]+=1
    return alfabet

n1=input()
n2=input()
if zlicz_znaki(n1) == zlicz_znaki(n2):
    print("TAK")
else:
    print("NIE")