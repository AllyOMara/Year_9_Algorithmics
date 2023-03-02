from gcd_recursive import *
# from gcd_recursive import gcd as gcd_rec
import unittest

class TestGCD(unittest.TestCase):

    def test_gcd(self):
        self.assertEqual(gcd(3,9), 3)
        self.assertEqual(gcd(21,9), 3)
        self.assertEqual(gcd(100,20), 20)
        self.assertEqual(gcd(11,9), 1)
        self.assertEqual(gcd(1,1), 1)
        self.assertEqual(gcd(0,0), 0)
        self.assertEqual(gcd(150,345), 15)

if __name__ == '__main__':
    unittest.main()