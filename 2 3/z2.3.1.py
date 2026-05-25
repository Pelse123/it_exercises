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
ile = int(input())
for i in range(ile):
    push(queue, int(input()))

min = front(queue)

while not isEmpty(queue):
    if min>front(queue):
        min = front(queue)
    pop(queue)

print(min)