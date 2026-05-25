ciag = input()
odwrocony = ""
for i in range(len(ciag)-1,-1,-1):
    odwrocony += ciag[i]
print(odwrocony)
if odwrocony.lower() == ciag.lower():
    print("Ten ciąg jest palindromem")
else:
    print("Ten ciąg nie jest palindromem")
slowo = ciag.lower()
print("a:",slowo.count("a"))
print("e:",slowo.count("e"))
print("i:",slowo.count("i"))
print("o:",slowo.count("o"))
print("u:",slowo.count("u"))