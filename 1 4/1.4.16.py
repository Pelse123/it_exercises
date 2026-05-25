def rzymska_na_arabska(n):
    wartosciarabskie = [1,5,10,50,100,500,1000]
    wartoscirzymskie = ["I","V","X","L","C","D","M"]
    wynik = 0
    poprzednia = 0
    for i in range(len(n)-1,-1,-1):
        for j in range(len(wartoscirzymskie)):
            if wartoscirzymskie[j] == n[i]:
                if wartosciarabskie[j]<poprzednia:
                    wynik -= wartosciarabskie[j]
                else:
                    wynik += wartosciarabskie[j]
                    poprzednia = wartosciarabskie[j]
    return wynik

rzymska = input()
print(rzymska_na_arabska(rzymska))