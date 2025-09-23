import unittest
from solution_ransom_note import Solution

fn = Solution().canConstruct

class Test(unittest.TestCase):

    def test_0(self):
        self.assertEqual(fn("aa", "aab"), True)

    def test_1(self):
        self.assertEqual(fn("a", "b"), False)

    def test_2(self):
        self.assertEqual(fn("aa", "ab"), False)

    def test_3(self):
        self.assertEqual(fn("ab", "baa"), True)
