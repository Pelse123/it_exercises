def scalanie(tablica,lewy_index,srodek,prawy_index,pomocnicza_tablica):
    for i in range(lewy_index,prawy_index+1):
        pomocnicza_tablica[i] = tablica[i]

    indexLewegoPodkreslenia =lewy_index
    indexPrawyPodkreslenia = srodek+1
    index_do_wpisania = lewy_index

    while(indexLewegoPodkreslenia<=srodek and indexPrawyPodkreslenia<=prawy_index):
        if pomocnicza_tablica[indexLewegoPodkreslenia]<=pomocnicza_tablica[indexPrawyPodkreslenia]:
            tablica[index_do_wpisania] = pomocnicza_tablica[indexLewegoPodkreslenia]
            index_do_wpisania +=1
            indexLewegoPodkreslenia +=1
        else:
            tablica[index_do_wpisania] = pomocnicza_tablica[indexPrawyPodkreslenia]
            index_do_wpisania +=1
            indexPrawyPodkreslenia +=1


    while indexLewegoPodkreslenia<=srodek:
        tablica[index_do_wpisania] = pomocnicza_tablica[indexLewegoPodkreslenia]
        index_do_wpisania += 1
        indexLewegoPodkreslenia += 1
    while indexPrawyPodkreslenia<=prawy_index:
        tablica[index_do_wpisania] = pomocnicza_tablica[indexPrawyPodkreslenia]
        index_do_wpisania += 1
        indexPrawyPodkreslenia += 1


def merge_sort(tablica,lewy_index,prawy_index,pomocnicza_tablica):
    if lewy_index < prawy_index:
        srodek = (lewy_index+prawy_index)//2
        merge_sort(tablica,lewy_index,srodek,pomocnicza_tablica)
        merge_sort(tablica,srodek+1,prawy_index,pomocnicza_tablica)
        scalanie(tablica,lewy_index,srodek,prawy_index,pomocnicza_tablica)

n = int(input())
tablica = []
for i in range(n):
    tablica.append(input())
lewy_index = 0
prawy_index = len(tablica)-1
pomocnicza_tablica = [0]*len(tablica)
merge_sort(tablica,lewy_index,prawy_index,pomocnicza_tablica)
for i in range(len(tablica)):
    print(tablica[i],end=" ")