def push(queue,wartosc):
    return queue.append(wartosc)

def pop(queue):
    return queue.pop(0)

def front(queue):
    return queue[0]

def back(queue):
    return queue[len(queue)-1]

def isEmpty(queue):
    return len(queue) == 0

def size(queue):
    return len(queue)

queue = []
slowo = input()
tablica_wystapien = []

for i in range(len(slowo)):
    push(queue,slowo[i])

tablica_wystapien = [0]*size(queue)

while not isEmpty(queue):
    literka = front(queue)
    for i in range(len(slowo)):
        if(literka == slowo[i]):
            tablica_wystapien[i] += 1
    pop(queue)

czy_jest_unikalna = False
for i in range(len(tablica_wystapien)):
    if tablica_wystapien[i] == 1:
        czy_jest_unikalna = True

if czy_jest_unikalna == False:
    print(-1)
else:
    for i in range(len(tablica_wystapien)):
        if(tablica_wystapien[i] == 1):
            print(i)
            break







