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


if __name__ == "__main__":
    unittest.main()
