"""
************************************************
 klasa: Rozne_funkcje()
 opis: Klasa wywołuje dwie metody statyczne jedną liczacą samogłoski w tekscie a drugą usuwającą powtórzenia
 metody: licz_samogłoski - zwraca licznik w którym jest zawarta ilość samogłosek w tekscie
 usun_powtórzenia - zwraca nowy_lancuch który  jest ciągiem tekstowym bez powtórzeń
 autor: 694202137
************************************************

"""
class Rozne_funkcje():
    @staticmethod
    def licz_samogloski(tekst):
        if tekst.strip() == "" or tekst.strip() == None:
            return 0
        samogloski = "aąeęiouóyAĄEĘIOUÓY"
        licznik =0
        for i in tekst:
            for j in samogloski:
                if i == j:
                    licznik = licznik + 1
        return licznik
    @staticmethod
    def usun_powtorzenia(tekst):
        if tekst.strip() == "" or tekst.strip() == None:
            return ""
        nowy_lancuch = ""
        nowy_lancuch+=tekst[0]
        for i in range (1,len(tekst)):
            if tekst[i] != tekst[i-1]:
                nowy_lancuch+=tekst[i]
        return nowy_lancuch
print(Rozne_funkcje.licz_samogloski(input("Wczytaj łańcuch do liczenia samogłosek: ")))
print(Rozne_funkcje.usun_powtorzenia(input("Wczytaj łańcuch do eliminacji duplikatów: ")))
