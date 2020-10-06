import unittest
from datetime import datetime, timedelta

from exercises.exercise_four import Promo


class ExerciseFouTests(unittest.TestCase):
    def test_is_no_expired(self):
        promo = Promo('2x1',  datetime.today() + timedelta(days=5))
        self.assertTrue(promo.expired)

    def test_is_expired(self):
        promo = Promo('Page 6 lleve 8', datetime.today() + timedelta(days=-5))
        self.assertFalse(promo.expired)


if __name__ == "__main__":
    unittest.main()
