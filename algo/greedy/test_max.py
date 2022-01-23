import unittest
from max_loot import maxloot


class TestMax(unittest.TestCase):
    def test_edx(self):
        W = 10
        n = 1
        tuples = [[500, 30]]
        result = maxloot(tuples, W, n)
        self.assertEqual(result[0], 166.666)


if __name__ == "__main__":
    unittest. main()
