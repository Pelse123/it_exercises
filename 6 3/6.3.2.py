n = int(input())
lista = []
for i in range(n):
    lista.append(input())
literka = input()
lista_z_literka = []
for i in range(len(lista)):
    if lista[i].lower().startswith(literka.lower()):
        lista_z_literka.append(lista[i])

for i in lista_z_literka:
    print(i)
lista_z_literka.sort()

print(";".join(lista_z_literka))

