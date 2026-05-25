zdanie = input()
zdanie_podzielone_na_elementy = zdanie.split(" ")

for i in range(len(zdanie_podzielone_na_elementy)):
    if zdanie_podzielone_na_elementy[i].isalpha():
        print("tylko litery")
    elif zdanie_podzielone_na_elementy[i].isdigit():
        print("tylko cyfry")
    elif zdanie_podzielone_na_elementy[i].isalnum():
        print("tylko litery i cyfry")
    else:
        print("inny typ")