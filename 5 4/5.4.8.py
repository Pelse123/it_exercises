def oblicz_hanoi_iteracyjnie(a,b,c,krazki):
    start = a+c
    wynik = ""
    l = ""
    p = ""
    ostatni_wynik = l + start + p
    for i in range(krazki):
        l = ""
        p = ""

        for j in range(len(ostatni_wynik)):
            if ostatni_wynik[j] == b:
                l = l+c
            elif ostatni_wynik[j] == c:
                l = l+b
            else:
                l = l+a

        for k in range(len(ostatni_wynik)):
            if ostatni_wynik[k] == b:
                p = p+a
            elif ostatni_wynik[k] == a:
                p = p+b
            else:
                p = p+c

        ostatni_wynik = l+start+p
    wynik += ostatni_wynik
    return wynik

a=input()
b=input()
c=input()
krazki = int(input())
print(oblicz_hanoi_iteracyjnie(a,b,c,krazki-1))