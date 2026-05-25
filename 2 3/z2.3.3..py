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

def czy_palindrom(queue,slowo):
    for i in range(len(queue)):
        if front(queue) != slowo[len(slowo) - 1 - i]:
            return False
        pop(queue)
    return True


queue = []
slowo = input()

for i in range(len(slowo)):
    push(queue,slowo[i])

if czy_palindrom(queue,slowo):
    print("Napis jest palindromem")
else:
    print("Napis nie jest palindromem")

