zdanie = input()
slowo = input().strip()
ilosc = zdanie.lower().count(slowo.lower())
if ilosc > 0:
    print(ilosc)
else:
    print("Słowo nie występuje w tekście")