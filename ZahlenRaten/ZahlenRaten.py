import random


class Zahlenraten():

    # Definiert alle benötigten Variablen

    def __init__(self) -> None:
        self.computer_zahl: int = random.randint(1000, 9999)
        self.bereits_gewonnen: bool = False
        self.versuche: int = 0
        self.geratene_zahl_liste: list[int] = []

    # zählt die versuche, schaut ob bereits gewonnen
    # legt die lsten für die beidenen jewaligen zahlen an

    def raten(self, geratene_zahl: int) -> None:
        self.versuche += 1
        self.bereits_gewonnen = (geratene_zahl == self.computer_zahl)

        self.geratene_zahl_liste = self.zahl_als_ziffern_liste(geratene_zahl)
        self.computer_zahl_liste = self.zahl_als_ziffern_liste(
            self.computer_zahl)

    # gibt ein True oder False zurück

    def wurde_bereits_gewonnen(self) -> bool:

        return self.bereits_gewonnen

    # gibt die Anzahl der Versche zurück

    def anzahl_versuche(self) -> int:

        return self.versuche

    # überprüft ob ob zewi zahlen mit dem gleichen Index das gleiche element haben
    # falls dies der fall ist füngen wir den index (an welcher stelle das ist) in eine liste in
    # Beispiel wir haben die Listen [1,2,3,4] und [1,3,2,4]
    # dann sieht mann das die erste und letzte zahl gleich sind
    # aus der funktion würden wir so eine liste bekommen [0, 3]
    # (beachte in PYthon wird mit 0 angefangen 0 ist die erste Stelle)

    def passende_stellen(self) -> list[int]:
        if self.geratene_zahl_liste == [0]:
            self.geratene_zahl_liste = [0, 0, 0, 0]
        ergebnis_liste: list[int] = []
        for idx, element in enumerate(self.geratene_zahl_liste):

            computer_ziffer = self.computer_zahl_liste[idx]
            geratene_ziffer = self.geratene_zahl_liste[idx]

            if computer_ziffer == geratene_ziffer:
                ergebnis_liste.append(idx)

        return ergebnis_liste

    #   gibt die liste zurück

    def zahl_als_ziffern_liste(self, zahl: int) -> list[int]:

        return list(map(int, str(zahl)))

    def wie_viele_stimmen_ueber_ein(self) -> int:
        count: int = 0
        for element in self.geratene_zahl_liste:
            if element in self.computer_zahl_liste:
                count += 1

        return count
