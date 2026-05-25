def push(queue,wartosc):
    queue.append(wartosc)
    return queue

def pop(queue):
    return queue.pop(0)

def isEmpty(queue):
    return len(queue)==0

def back(queue):
    return queue[-1]

def front(queue):
    return queue[0]

def size(queue):
    return len(queue)

def dodaj_naprzemiennie(kolejka1,kolejka2):
    kolejka_naprzemienna = []
    dlugosc = max(size(kolejka1), size(kolejka2))
    for i in range(dlugosc):
        if isEmpty(kolejka1)==False:
            push(kolejka_naprzemienna,front(kolejka1))
            pop(kolejka1)
        if isEmpty(kolejka2)==False:
            push(kolejka_naprzemienna,front(kolejka2))
            pop(kolejka2)
    return kolejka_naprzemienna

def wyswietl_kolejke(kolejka):
    for i in range(size(kolejka)):
        print(front(kolejka),end=" ")
        pop(kolejka)


m = int(input())
n = int(input())
kolejka_m = []
kolejka_n = []

for i in range(m):
    push(kolejka_m,int(input()))

for i in range(n):
    push(kolejka_n,int(input()))

wyswietl_kolejke(dodaj_naprzemiennie(kolejka_m,kolejka_n))


