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
    zamowienie = {"nr_stolika":int(input()),"danie":input()}
    push(queue,zamowienie)

while not isEmpty(queue):
    zamowienie = front(queue)
    print(f"Zamówienie dla stolika {zamowienie['nr_stolika']}: {zamowienie['danie']}")
    pop(queue)