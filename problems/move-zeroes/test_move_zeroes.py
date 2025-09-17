import unittest
from solution_move_zeroes import Solution

fn = Solution().moveZeroes

class Test(unittest.TestCase):

    def test_0(self):
        numsbefore = [0]
        numsafter = [0]
        self.assertEqual(fn(numsbefore), numsafter)


    def test_1(self):
        numsbefore = [0,1,0,3,12]
        numsafter = [1,3,12,0,0]
        self.assertEqual(fn(numsbefore), numsafter)

    def test_2(self):
        numsbefore = [2,1]
        numsafter = [2,1]
        self.assertEqual(fn(numsbefore), numsafter)

    def test_3(self):
        numsbefore = [2, 1, 7, 0]
        numsafter = [2, 1, 7, 0]
        self.assertEqual(fn(numsbefore), numsafter)

    def test_3(self):
        numsbefore = [0, 2, 1, 7, 0]
        numsafter = [2, 1, 7, 0, 0]
        self.assertEqual(fn(numsbefore), numsafter)

    def test_4(self):
        numsbefore = [1, 0, 1]
        numsafter = [1, 1, 0]
        self.assertEqual(fn(numsbefore), numsafter)
