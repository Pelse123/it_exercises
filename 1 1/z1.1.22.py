wagakg = float(input())
wzrostmt = float(input())
wynik = wagakg/(wzrostmt**2)
wynik = round(wynik, 2)
if(wynik < 18.5):
    print(wynik)
    print("Niedowaga")
elif(wynik >= 18.5 and wynik < 25):
    print(wynik)
    print("Waga prawidłowa")
elif(wynik >= 25 and wynik < 30):
    print(wynik)
    print("Nadwaga")
else:
    print(wynik)
    print("Otyłość")