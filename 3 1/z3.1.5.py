tab=[5,2,4,9,7,1,6]#9,7
n = len(tab)
if tab[0]>tab[1]:
    maksymalna = tab[0]
    druga_maksymalna = tab[1]
else:
    maksymalna = tab[1]
    druga_maksymalna = tab[0]
for i in range(2,n):
    if tab[i] > maksymalna:
        druga_maksymalna = maksymalna
        maksymalna = tab[i]
    elif tab[i] > druga_maksymalna and tab[i] < maksymalna:
        druga_maksymalna = tab[i]
print(maksymalna)
print(druga_maksymalna)

"""
jeżeli tab[1] > tab[2]
    maksymalna <- tab[1]
    druga_maksymalna <- tab[2]
w przeciwnym wypadku
    maksymalna <- tab[2]
    druga_maksymalna <- tab[1]
dla i = 3,4,5...n wykonuj
    jezeli tab[i]>maksymalna
        druga_maksymalna <- maksymalna
        maksymalna <- tab[i]
    w przeciwnym wypadku jeżeli tab[i]>druga_maksymalna 
        druga_maksymalna <- tab[i]
wypisz druga_maksymalna
"""

