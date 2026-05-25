def czy_podzielna_przez_3_i_5(n):
    return (n%3==0 and n%5==0)

liczba = int(input())

if (czy_podzielna_przez_3_i_5(liczba)):
    print("Liczba jest podzielna przez 3 i 5 jednoczesnie")
else:
    print("Liczba nie jest podzielna przez 3 i 5 jednoczesnie")