miesiac = int(input())
if(miesiac == 1):
    print("Styczen")
elif(miesiac == 2):
    print("Luty")
elif(miesiac == 3):
    print("Marzec")
elif(miesiac == 4):
    print("Kwiecień")
elif(miesiac == 5):
    print("Maj")
elif(miesiac == 6):
    print("Czerwiec")
elif(miesiac == 7):
    print("Lipiec")
elif(miesiac == 8):
    print("Sierpien")
elif(miesiac == 9):
    print("Wrzesien")
elif(miesiac == 10):
    print("Pazdziernik")
elif(miesiac == 11):
    print("Listopad")
elif(miesiac == 12):
    print("Grudzien")
else:
    print("Podana niepoprawna wartosc")

#sposob2

if miesiac>0 and miesiac<13:
    miesiace = ["Styczen", "Luty", "Marzec", "Kwiecien", "Maj", "Czerwiec", "Lipiec", "Sierpien", "Wrzesien",
                "Pazdzienik", "Listopad", "Grudzien"]
    print(miesiace[miesiac - 1])
else:
    print("Niepoprawna wartosc")