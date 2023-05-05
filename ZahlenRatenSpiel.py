from ZahlenRaten.ZahlenRaten import Zahlenraten


def Spielen():

    sp = ZahlenRatenSpiel()

    sp.Anfang()


class ZahlenRatenSpiel():

    def __init__(self) -> None:

        self.zr = Zahlenraten()

    def Anfang(self):

        print("Hallo")

        self.erklärung_gefordert()

    def generator_hinweis(self):
        geanderte_zahl = map(self.zr.passende_stellen, self.umwandeln())
        print("Es stimmen " +
              1 + " überein")
        print(self.zr.passende_stellen())
        print(self.zr.wie_viele_stimmen_ueber_ein())

    def umwandeln(self, n):

        n = n + 1
        return str(n)

    def erklärung_gefordert(self):

        erklärung_gefordert = input("Möchtest du eine Erklärung (j/n): ")

        if erklärung_gefordert == "j":
            self.erklärung()

        if erklärung_gefordert == "n":
            self.spiel()

    def erklärung(self):

        print("Hier ist die Erklärung")
        print(
            """Spielprinzip:
            \n- Der Computer denkt sich eine Zahl zwischen 1000 und 9999 aus
            \n- dann ratest du eine Zahl in dem selben zahlen Bereich
            \n- als nächtest bekommst du zwei Hinweise
            \n- das solange bist du gewonnen hast \n """)
        print(
            """Der erste Hinweis ist ob eine Ziffer an der richtigen Stelle ist
            \nBeispiel:
            \n- Computerzahl: [8064] Deine Zahl: [8923]
            \n- damit würdest du den Hinweis bekommen: Die Stelle/n 0 stimm/en überein
            \nDer zweite hinweis gibt an wie viele Ziffern aus deiner Zahl in der Geheimzahl sind
            \n Mit dem Beispiel von gerade eben würdest du bekommen:
            \n- Es ist/sind 1 Ziffer gemeinsam""")
        input("Tippe Enter wenn du spielen willst: ")

        self.spiel()

    def spiel(self):

        while not self.zr.wurde_bereits_gewonnen():

            self.geratene_zahl: str = input(
                "Gib eine 4 stellige Zahl ein im Bereich 1000-9999 ein: ")
            self.Prüfen_zahl()
            while self.geratene_zahl.isnumeric() == False:

                self.geratene_zahl = input("NUR ZAHLEN DU IDIOT! ")

            self.zr.raten(int(self.geratene_zahl))

            if self.zr.wurde_bereits_gewonnen():

                break

            else:

                self.generator_hinweis()

        print("Du hast gewonnen")
        print("Du hast " + str(self.zr.anzahl_versuche()) + " gebraucht")

    def Prüfen_zahl(self):
        while int(self.geratene_zahl) < 1000 or int(self.geratene_zahl) > 9999:
            self.geratene_zahl = input(
                "Du musst eine zahl zwischen 1000 und 9999 ein geben: ")


Spielen()


# Beobachtung:
# bei 0000 leere liste aber eins richtig sollte unmöglich sein
