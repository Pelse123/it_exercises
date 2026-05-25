pierwszywyraz= int(input())
roznica= int(input())
iloscelementow= int(input())
ciag = [pierwszywyraz]

for i in range(1,iloscelementow):
    ciag.append(ciag[i-1]+roznica)

for i in range(iloscelementow):
    print(ciag[i])