def generujMacierz(n):
    macierz = [[n*j+i-n for i in range(1,n+1)]for j in range(1,n+1)]
    return macierz

print(generujMacierz(int(input())))
