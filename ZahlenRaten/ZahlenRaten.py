import random


class Zahlenraten():

    def __init__(self) -> None:
        self.computer_zahl: int = random.randint(1000, 9999)
        self.bereits_gewonnen: bool = False
        self.versuche: int = 0

    def raten(self, geratene_zahl: int) -> None:
        self.versuche += 1
        self.bereits_gewonnen = (geratene_zahl == self.computer_zahl)

        self.geratene_zahl_liste = self.zahl_als_ziffern_liste(geratene_zahl)
        self.computer_zahl_liste = self.zahl_als_ziffern_liste(
            self.computer_zahl)

    def wurde_bereits_gewonnen(self) -> bool:

        return self.bereits_gewonnen

    def anzahl_versuche(self) -> int:

        return self.versuche

    def passende_stellen(self) -> list[int]:
        ergebnis_liste: list[int] = []
        for idx, element in enumerate(self.geratene_zahl_liste):

            computer_ziffer = self.computer_zahl_liste[idx]
            geratene_ziffer = self.geratene_zahl_liste[idx]

            if computer_ziffer == geratene_ziffer:
                ergebnis_liste.append(idx)

        return ergebnis_liste

    def zahl_als_ziffern_liste(self, zahl: int) -> list[int]:

        return list(map(int, str(zahl)))
