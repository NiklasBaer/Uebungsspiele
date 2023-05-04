import unittest

from ZahlenRaten.ZahlenRaten import Zahlenraten
import unittest.mock as mock


def return_test_number(untergrenze, obergrenze):
    return 1234


class TestZahlenRaten(unittest.TestCase):

    def test_gleich_richtig_geraten(self):
        with mock.patch("random.randint", return_test_number):
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
        with mock.patch("random.randint", return_test_number):
            zr = Zahlenraten()
            zr.raten(4321)
            self.assertFalse(zr.wurde_bereits_gewonnen())

    def test_keine_passenden_stellen(self):

        with mock.patch("random.randint", return_test_number):
            zr = Zahlenraten()
            zr.raten(4321)
            self.assertEqual(zr.passende_stellen(), [])

    def test_eine_passende_stelle(self):
        with mock.patch("random.randint", return_test_number):
            zr = Zahlenraten()
            zr.raten(1325)
            self.assertEqual(zr.passende_stellen(), [0])

    def test_mehrere_passende_stellen(self):
        with mock.patch("random.randint", return_test_number):
            zr = Zahlenraten()
            zr.raten(1324)
            self.assertEqual(zr.passende_stellen(), [0, 3])

    def test_nichts_raten(self):
        with mock.patch("random.randint", return_test_number):
            zr = Zahlenraten()
            self.assertEqual(zr.passende_stellen(), [])

    def test_wie_viel_stimmt_ueber_ein(self):
        with mock.patch("random.randint", return_test_number):
            zr = Zahlenraten()
            zr.raten(4321)
            self.assertEqual(zr.wie_viele_stimmen_ueber_ein(), 4)

    def test_vergessen_zu_raten(self):
        with mock.patch("random.randint", return_test_number):
            zr = Zahlenraten()
            self.assertEqual(zr.wie_viele_stimmen_ueber_ein(), 0)

    def test_keine_uebereinstimmung(self):
        with mock.patch("random.randint", return_test_number):
            zr = Zahlenraten()
            zr.raten(0000)
            self.assertEqual(zr.wie_viele_stimmen_ueber_ein(), 0)

    def test_eine_uebereinstimmung(self):
        with mock.patch("random.randint", return_test_number):
            zr = Zahlenraten()
            zr.raten(1000)
            self.assertEqual(zr.wie_viele_stimmen_ueber_ein(), 1)


if __name__ == "__main__":
    unittest.main()
