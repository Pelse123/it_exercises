class Urzadzenie:
    """
    ************************************************
    nazwa: zwroc_komunikat
    opis: wyswietla napis podany w argumencie metody
    parametry: komunikat - argument metody który jest wypisywany
    zwracany typ i opis: brak
    autor: 694202137
    ************************************************
    """
    @staticmethod
    def zwroc_komunikat(komunikat):
        print(komunikat)

class Pralka(Urzadzenie):
    def __init__(self,):
        self.__nr_prania:int = 0

    def ustaw_pranie(self,numer):
        if (numer>=1 and numer<=12):
            self.__nr_prania = numer
        else:
            self.__nr_prania = 0
        return self.__nr_prania

class Odkurzacz(Urzadzenie):
    def __init__(self):
        self.__stan_odkurzacza = False

    def on(self):
        if self.__stan_odkurzacza==False:
            self.__stan_odkurzacza = True
            self.zwroc_komunikat("Odkurzacz włączono")

    def off(self):
        if self.__stan_odkurzacza:
            self.__stan_odkurzacza = False
            self.zwroc_komunikat("Odkurzacz wyłączono")

Obiekt_pralka = Pralka()
Obiekt_odkurzacz =Odkurzacz()

if Obiekt_pralka.ustaw_pranie(2) == 0:
    print("Podano niepoprawny numer programu")
else:
    print("Program został ustawiony")

if Obiekt_pralka.ustaw_pranie(13) == 0:
    print("Podano niepoprawny numer programu")
else:
    print("Program został ustawiony")

Obiekt_odkurzacz.on()
Obiekt_odkurzacz.on()
Obiekt_odkurzacz.on()
Urzadzenie.zwroc_komunikat("Odkurzacz wyładował się")
Obiekt_odkurzacz.off()