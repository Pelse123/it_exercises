n = int(input())
i = 0
T=[]
T.append(n)
while True:
    k = T[i]
    suma = 0
    while k>0:
        suma += (k%10)*(k%10)
        k = k//10
    if suma==1:
        print("Liczba wesoła hihi")
        exit()
    for j in range(i+1):
        if T[j]==suma:
            print("liczba smutna :(")
            exit()
    i = i+1
    T.append(suma)
    print(T)

