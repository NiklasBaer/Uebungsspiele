from ZahlenRaten.ZahlenRaten import Zahlenraten


def Spielen():

    sp = ZahlenRatenSpiel()

    sp.start()


class ZahlenRatenSpiel():

    def __init__(self) -> None:

        self.zr = Zahlenraten()

    def start(self):

        print("Hallo")

        erklärung_gefordert = input("Möchtest du eine Erklärung (j/n)")

        print("")

        if erklärung_gefordert == "j":

            self.erklaerung()

        elif erklärung_gefordert == "n":

            print("Das spiel geht los")

        while not self.zr.wurde_bereits_gewonnen():

            geratene_zahl: str = input("Gib eine 4 stellige Zahl ein ")

            while geratene_zahl.isnumeric() == False:

                geratene_zahl = input("NUR ZAHLEN DU IDIOT! ")

            self.zr.raten(int(geratene_zahl))

            if self.zr.wurde_bereits_gewonnen():

                break

            else:

                self.generator_hinweis()

        print("Du hast gewonnen")

    def erklaerung(self):

        print("Hier ist die Erklärung")

        input("Wenn du bereit bist tppe Enter ")

    def generator_hinweis(self):
        print(self.zr.passende_stellen())
        print(self.zr.wie_viele_stimmen_ueber_ein())


Spielen()
