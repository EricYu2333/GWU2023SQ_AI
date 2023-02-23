import unittest
import time
from pitchers import Pitchers

class TestCalculator(unittest.TestCase):

    def TestFile(self, filename):
        pitchers = Pitchers()
        start_time = time.time()
        steps, node = pitchers.Astar_Search(filename)
        end_time = time.time()
        print(f"File name: {filename}")
        print(f"Pitchers capacities: {node.capacities[:-1]}")
        print(f"Target: {node.capacities[-1]}")
        print(f"Steps: {steps}")
        if node:
            print(f"Path: {node.path}")
        else:
            print(f"Path: No Path!")
        print(f"Time cost: {format(end_time - start_time, '.3f')}s\n")
        return steps

    def testSearch01(self):
        result = self.TestFile("input1.txt")
        self.assertEqual(result,4)

    def testSearch02(self):
        result = self.TestFile("input2.txt")
        self.assertEqual(result,7)

    def testSearch03(self):
        result = self.TestFile("input3.txt")
        self.assertEqual(result,5)

    def testSearch04(self):
        result = self.TestFile("input4.txt")
        self.assertEqual(result,10)

    def testSearch05(self):
        result = self.TestFile("input5.txt")
        self.assertEqual(result,7)

    def testSearch06(self):
        result = self.TestFile("input6.txt")
        self.assertEqual(result,7)

    def testSearch07(self):
        result = self.TestFile("input7.txt")
        self.assertEqual(result,10)

    def testSearch08(self):
        result = self.TestFile("input8.txt")
        self.assertEqual(result,20)

    def testSearch09(self):
        result = self.TestFile("input9.txt")
        self.assertEqual(result,20)

if __name__ == '__main__':
    unittest.main()
