try:
    numer = input()
    if numer[0]!="+":
        numer = int(numer)
        if(len(str(numer))==9):
            print("Poprawny numer telefonu")
        else:
            raise TypeError("Niepoprawny numer telefonu")
    else:
        numer = numer.split(sep=" ")
        przekierowanie = numer[0]
        numer_telefonu = int(numer[1])
        if len(str(numer_telefonu))==9:
            print("Poprawny numer telefonu")
        else:
            raise TypeError("Niepoprawny numer telefonu")

except TypeError as e:
    print(e)
except ValueError as e:
    print("Niepoprawny numer telefonu")