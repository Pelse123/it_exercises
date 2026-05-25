def czy_przyjaciolki(a,b):
    suma_a = 0
    suma_b = 0
    while a!=0:
        suma_a += a%10
        a=a//10
    while b!=0:
        suma_b += b%10
        b=b//10
    if suma_a==suma_b:
        return True
    return False

def czy_dobre_przyjaciolki(a,b):
    if czy_przyjaciolki(a,b):
        pierwsza_a = 0
        temp_a = a
        while temp_a!=0:
            pierwsza_a = temp_a%10
            temp_a = temp_a//10
        pierwsza_b = 0
        temp_b = b
        while temp_b!=0:
            pierwsza_b = temp_b%10
            temp_b = temp_b//10
        ostatnia_a = a%10
        ostatnia_b = b%10
        if ostatnia_a==pierwsza_b or ostatnia_b==pierwsza_a:
            return True
    return False

a = int(input())
b = int(input())
print(czy_przyjaciolki(a,b))
print(czy_dobre_przyjaciolki(a,b))