import random
import unittest

class Test(unittest.TestCase):
    def test(self):
        tab = [0] * 100
        tab_test=[0] * 100
        for i in range(100):
            ran = random.randint(1, 1000)
            tab[i] = ran
            tab_test[i] = ran
        sortowanie_babelkowe(tab)
        self.assertEqual(tab, sorted(tab_test),True)


def sortowanie_babelkowe(tablica):
    n = len(tablica)
    for i in range(n):
        flaga = True
        for j in range(n-1-i):
            if tablica[j]>tablica[j+1]:
                flaga = False
                temp = tablica[j]
                tablica[j] = tablica[j+1]
                tablica[j+1] = temp
        if flaga:
             break

tab = [0]*100

for i in range(100):
    tab[i] = random.randint(1,1000)
sortowanie_babelkowe(tab)
print("Posortowana tablica: ")
for i in range(100):
    if i!=99:
        print(tab[i],end=",")
    else:
        print(tab[i])
