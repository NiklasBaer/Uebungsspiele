import random


class Zahlenraten():

    def __init__(self) -> None:
        self.computer_zahl: int = random.randint(1000, 9999)
        self.bereits_gewonnen: bool = False
        self.versuche: int = 0

    def raten(self, geratene_zahl: int) -> None:
        self.versuche += 1
        self.bereits_gewonnen = (geratene_zahl == self.computer_zahl)

    def wurde_bereits_gewonnen(self) -> bool:
        return self.bereits_gewonnen

    def anzahl_versuche(self) -> int:

        return self.versuche

    def passende_stellen(self) -> list[int]:
        pass
