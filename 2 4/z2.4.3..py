def wspolneZakupy(lista_zakupow):
    wspolne = lista_zakupow[0]
    for i in range(1,len(lista_zakupow)):
        wspolne = wspolne & lista_zakupow[i]
    return wspolne

zakupy_A = {"mleko", "chleb", "maslo", "jajka"}
zakupy_B = {"mleko", "jajka", "ser"}
zakupy_C = {"mleko", "jajka", "maslo"}
zakupy_D = {"chleb", "sok", "jajka", "mleko"}
lista_zakupow = [zakupy_A, zakupy_B, zakupy_C, zakupy_D]

print(wspolneZakupy(lista_zakupow))