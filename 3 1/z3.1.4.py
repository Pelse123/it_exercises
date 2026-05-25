tablica=[0,1,4,2,45]
n = len(tablica)-1

i = 1
j = n
while i < j:
    temp = tablica[i]
    tablica[i] = tablica[j]
    tablica[j] = temp
    i += 1
    j -= 1
print(tablica)

"""
i <- 1
j <- n
dopóki i<j
    temp <- tablica[i]
    tablica[i] <- tablica[j]
    tablica[j] <- temp
    i <- i+1
    j <- j-1
wypisz tablica
"""
