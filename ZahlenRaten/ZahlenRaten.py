import random


class Zahlenraten():

    def __init__(self) -> None:
        self.computer_zahl = random.randint(1000, 9999)
        self.bereits_gewonnen = False

    def raten(self, geratene_zahl: int) -> None:

        self.bereits_gewonnen = (geratene_zahl == self.computer_zahl)

    def wurde_bereits_gewonnen(self) -> bool:
        return self.bereits_gewonnen

    def anzahl_versuche(self) -> int:
        pass
