import unittest

from ZahlenRaten.ZahlenRaten import Zahlenraten
import unittest.mock as mock


def zurückgabe_der_test_nummer(untergrenze, obergrenze):
    return 1234


def test_nummer_mit_zwei_gleichen_ziffern(untergrenze, obergrenze):
    return 1231


def test_nummer_mit_drei_gleichen_ziffern(untergrenze, obergrenze):
    return 1211


def test_wenn_nummer_nur_aus_einer_zahl(untergrenze, obergrenze):
    return 1111


def test_bug(untergenze, obergerenze):
    return 8064


def test_bug2(untergenze, obergerenze):
    return 8064


class TestZahlenRaten(unittest.TestCase):

    def test_gleich_richttest_nummer_mit_zewi_gleichen_ziffernig_geraten(self):
        with mock.patch("random.randint", zurückgabe_der_test_nummer):
            zr = Zahlenraten()
            zr.raten(1234)
            self.assertTrue(zr.wurde_bereits_gewonnen())

    def test_anzahl_der_versuche(self):

        zr = Zahlenraten()
        zr.anzahl_versuche()
        zr.raten(1234)
        zr.raten(329429)
        self.assertEqual(zr.anzahl_versuche(), 2)

    def test_falsch_geraten(self):
        with mock.patch("random.randint", zurückgabe_der_test_nummer):
            zr = Zahlenraten()
            zr.raten(4321)
            self.assertFalse(zr.wurde_bereits_gewonnen())

    def test_keine_passenden_stellen(self):

        with mock.patch("random.randint", zurückgabe_der_test_nummer):
            zr = Zahlenraten()
            zr.raten(4321)
            self.assertEqual(zr.passende_stellen(), [])

    def test_eine_passende_stelle(self):
        with mock.patch("random.randint", zurückgabe_der_test_nummer):
            zr = Zahlenraten()
            zr.raten(1325)
            self.assertEqual(zr.passende_stellen(), [0])

    def test_mehrere_passende_stellen(self):
        with mock.patch("random.randint", zurückgabe_der_test_nummer):
            zr = Zahlenraten()
            zr.raten(1324)
            self.assertEqual(zr.passende_stellen(), [0, 3])

    def test_nichts_raten(self):
        with mock.patch("random.randint", zurückgabe_der_test_nummer):
            zr = Zahlenraten()
            self.assertEqual(zr.passende_stellen(), [])

    def test_wie_viel_stimmt_ueber_ein(self):
        with mock.patch("random.randint", zurückgabe_der_test_nummer):
            zr = Zahlenraten()
            zr.raten(4321)
            self.assertEqual(zr.wie_viele_stimmen_ueber_ein(), 4)

    def test_vergessen_zu_raten(self):
        with mock.patch("random.randint", zurückgabe_der_test_nummer):
            zr = Zahlenraten()
            self.assertEqual(zr.wie_viele_stimmen_ueber_ein(), 0)

    def test_keine_uebereinstimmung(self):
        with mock.patch("random.randint", zurückgabe_der_test_nummer):
            zr = Zahlenraten()
            zr.raten(0000)
            self.assertEqual(zr.wie_viele_stimmen_ueber_ein(), 0)

    def test_eine_uebereinstimmung(self):
        with mock.patch("random.randint", zurückgabe_der_test_nummer):
            zr = Zahlenraten()
            zr.raten(1000)
            self.assertEqual(zr.wie_viele_stimmen_ueber_ein(), 1)

    def test_zwei_uebereinstimmen(self):
        with mock.patch("random.randint", test_nummer_mit_zwei_gleichen_ziffern):
            zr = Zahlenraten()
            zr.raten(1450)
            self.assertEqual(zr.wie_viele_stimmen_ueber_ein(), 1)

    def test_drei_uebereinstimmen(self):
        with mock.patch("random.randint", test_nummer_mit_zwei_gleichen_ziffern):
            zr = Zahlenraten()
            zr.raten(1450)
            self.assertEqual(zr.wie_viele_stimmen_ueber_ein(), 1)

    def test_zwei_uebereinstimmung(self):
        with mock.patch("random.randint", zurückgabe_der_test_nummer):
            zr = Zahlenraten()
            zr.raten(1190)
            self.assertEqual(zr.wie_viele_stimmen_ueber_ein(), 2)

    def test_alle_richtig(self):
        with mock.patch("random.randint", test_wenn_nummer_nur_aus_einer_zahl):
            zr = Zahlenraten()
            zr.raten(1111)
            self.assertEqual(zr.wie_viele_stimmen_ueber_ein(), 4)

    def test_drei_richtig(self):
        with mock.patch("random.randint", test_nummer_mit_drei_gleichen_ziffern):
            zr = Zahlenraten()
            zr.raten(1011)
            self.assertEqual(zr.wie_viele_stimmen_ueber_ein(), 3)

    def test_alles_null(self):
        with mock.patch("random.randint", test_bug):
            zr = Zahlenraten()
            zr.raten(0000)
            self.assertEqual(zr.passende_stellen(), [1])

    def test_wenn_fuerende_nullen(self):
        with mock.patch("random.randint", test_bug):
            zr = Zahlenraten()
            zr.raten(int("0003"))
            self.assertEqual(zr.passende_stellen(), [1])


if __name__ == "__main__":
    unittest.main()
