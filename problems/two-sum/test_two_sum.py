import unittest
from solution_two_sum import Solution

fn = Solution().twoSum

class Test(unittest.TestCase):

    def test_0(self):
        self.assertEqual(fn(nums = [3,3], target = 6), [0, 1])

    def test_1(self):
        self.assertEqual(fn(nums = [-1,-2,-3,-4], target = -8), None)

    def test_2(self):
        self.assertEqual(fn(nums = [1000000000, 1000000000], target = 2000000000), [0, 1])

    def test_3(self):
        self.assertEqual(fn(nums = [1,5,7,9], target = 10), [0, 3])

    def test_4(self):
        self.assertEqual(fn(nums = [1,2,3,4,5,6,7,8,9,10], target = 3), [0, 1])

    def test_5(self):
        self.assertEqual(fn(nums = [0,4,3,0], target = 0), [0, 3])

    def test_6(self):
        self.assertEqual(fn(nums = [1000000000, -1000000000, 500000000, -500000000], target = 0), [0, 1])
