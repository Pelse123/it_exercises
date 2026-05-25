def znajdzNajdluzszeSlowo(lista):
    return max(lista, key= lambda x: len(x))
n = int(input())
tablica = [input() for i in range(n)]
print(znajdzNajdluzszeSlowo(tablica))