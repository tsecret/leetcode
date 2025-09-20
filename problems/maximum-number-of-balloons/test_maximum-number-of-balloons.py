import unittest
from solution_maximum_number_of_balloons import Solution

fn = Solution().maxNumberOfBalloons

class Test(unittest.TestCase):

    def test_0(self):
        self.assertEqual(fn('nlaebolko'), 1)

    def test_1(self):
        self.assertEqual(fn('loonbalxballpoon'), 2)

    def test_2(self):
        self.assertEqual(fn('leetcode'), 0)

    def test_3(self):
        self.assertEqual(fn('krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw'), 10)

    def test_4(self):
        self.assertEqual(fn('"lloo"'), 0)

    def test_5(self):
        self.assertEqual(fn('balon'), 0)
