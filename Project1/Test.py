import unittest
from pitchers import Pitchers

class TestCalculator(unittest.TestCase):
    def testSearch01(self):
        pitchers = Pitchers()
        result = pitchers.SearchPath("input1.txt")
        self.assertEqual(result,7)

    def testSearch02(self):
        pitchers = Pitchers()
        result = pitchers.SearchPath("input2.txt")
        self.assertEqual(result,-1)

    def testSearch03(self):
        pitchers = Pitchers()
        result = pitchers.SearchPath("input3.txt")
        self.assertEqual(result,-1)

    def testSearch04(self):
        pitchers = Pitchers()
        result = pitchers.SearchPath("input4.txt")
        self.assertEqual(result,36)

    def testSearch05(self):
        pitchers = Pitchers()
        result = pitchers.SearchPath("input5.txt")
        self.assertEqual(result,5)

    def testSearch06(self):
        pitchers = Pitchers()
        result = pitchers.SearchPath("input6.txt")
        self.assertEqual(result,5)

if __name__ == '__main__':
    unittest.main()
