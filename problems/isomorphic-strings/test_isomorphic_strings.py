import unittest
from solution_isomorphic_strings import Solution

fn = Solution().isIsomorphic

class Test(unittest.TestCase):

    def test_0(self):
        self.assertEqual(fn(s = "hello", t = "world"), False)

    # def test_1(self):
    #     self.assertEqual(fn(s = "abcdefghijklmnopqrstuvwxyz", t = "zyxwvutsrqponmlkjihgfedcba"), True)

    # def test_2(self):
    #     self.assertEqual(fn(s = "paper", t = "title"), True)

    # # def test_3(self):
    # #     self.assertEqual(fn(s = "#a@C", t = "%b$D"), True)

    # def test_4(self):
    #     self.assertEqual(fn(s = "1234567890", t = "0987654321"), True)

    # def test_5(self):
    #     self.assertEqual(fn(s = "aaaa", t = "bbbb"), True)

    # def test_6(self):
    #     self.assertEqual(fn(s = "123", t = "456"), True)

    # def test_7(self):
    #     self.assertEqual(fn(s = "13", t = "42"), True)

    # def test_8(self):
    #     self.assertEqual(fn(s = "egg", t = "add"), True)

    # def test_9(self):
    #     self.assertEqual(fn(s = "test", t = "tets"), False)

    # def test_10(self):
    #     self.assertEqual(fn(s = "foo", t = "bar"), False)

    # def test_11(self):
    #     self.assertEqual(fn(s = "badc", t = "baba"), False)

    # def test_12(self):
    #     self.assertEqual(fn(s = "abba", t = "abba"), True)

    # def test_13(self):
    #     self.assertEqual(fn(s = "a", t = "a"), True)

    # def test_14(self):
    #     self.assertEqual(fn(s = "abcd", t = "dcba"), True)

    # def test_15(self):
    #     self.assertEqual(fn(s = "ab", t = "aa"), False)

    # def test_16(self):
    #     self.assertEqual(fn(s = "abcdefghijabcdefghij", t = "zyxwvutsrqzyxwvutsrq"), True)

    # def test_17(self):
    #     self.assertEqual(fn(s = "testcase", t = "tattldce"), False)

    # def test_18(self):
    #     self.assertEqual(fn(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz", t = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzz"), False)

    # def test_19(self):
    #     self.assertEqual(fn(s = "thisisatest", t = "qdpdqpdafqd"), False)

    # def test_20(self):
    #     self.assertEqual(fn(s = "123456", t = "654321"), True)

    # def test_21(self):
    #     self.assertEqual(fn(s = "hello world", t = "uifsf ftuqi"), False)

    # def test_22(self):
    #     self.assertEqual(fn(s = "aba", t = "cdc"), True)

    # def test_23(self):
    #     self.assertEqual(fn(s = "xyzzzzzzzzzyxzzzzzzzxy", t = "yxqqqqqqqqqyxqqqqqqqyx"), False)

    # def test_24(self):
    #     self.assertEqual(fn(s = "aabbccddeeff", t = "zzyyxxwwvvuuzz"), True)

    # def test_25(self):
    #     self.assertEqual(fn(s = "aabb", t = "cccc"), False)

    # def test_26(self):
    #     self.assertEqual(fn(s = "abracadabra", t = "xyxzyzyxzyx"), False)

    # def test_27(self):
    #     self.assertEqual(fn(s = "aaaaa", t = "bbbbb"), True)

    # def test_28(self):
    #     self.assertEqual(fn(s = "abcdeabcde", t = "fghijfghij"), True)

    # def test_29(self):
    #     self.assertEqual(fn(s = "abcdefg", t = "gfedcba"), True)

    # def test_30(self):
    #     self.assertEqual(fn(s = "a", t = "z"), True)

    # def test_31(self):
    #     self.assertEqual(fn(s = "abacaba", t = "xyzxzyx"), False)

    # def test_32(self):
    #     self.assertEqual(fn(s = "abccbaabc", t = "xyzyxzyxzyx"), False)

    # def test_33(self):
    #     self.assertEqual(fn(s = "abcdabcdabcd", t = "wxyzwxyzwxyz"), True)

    # def test_34(self):
    #     self.assertEqual(fn(s = "mississippi", t = "bbccddeffgg"), False)

    # def test_35(self):
    #     self.assertEqual(fn(s = "aabbccddeeff", t = "zzzzyyxxwwvvuuzz"), False)

    # def test_36(self):
    #     self.assertEqual(fn(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz", t = "zzyyxxwwvvuuttrrssqqppoonnmmllkkjjiihhggeeffddeebbaa"), False)

    # def test_37(self):
    #     self.assertEqual(fn(s = "abcde", t = "edcba"), True)

    # def test_38(self):
    #     self.assertEqual(fn(s = "ababab", t = "xyzxyz"), False)

    # def test_39(self):
    #     self.assertEqual(fn(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz", t = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba"), False)

    # def test_40(self):
    #     self.assertEqual(fn(s = "ababababab", t = "cdcdcdcdcd"), True)

    # def test_41(self):
    #     self.assertEqual(fn(s = "randomstring", t = "stringrandom"), False)

    # def test_42(self):
    #     self.assertEqual(fn(s = "mississippi", t = "hhlllppppss"), False)

    # def test_43(self):
    #     self.assertEqual(fn(s = "aabbccddeeffgg", t = "zzxxccvvnngghh"), True)

    # def test_44(self):
    #     self.assertEqual(fn(s = "repeatedcharacters", t = "substitutedletters"), False)

    # def test_45(self):
    #     self.assertEqual(fn(s = "aabbcc", t = "ddeeff"), True)

    # def test_46(self):
    #     self.assertEqual(fn(s = "abcdefghijkabcdefghijkabcdefghijkabcdefghijk", t = "abcdefghijkabcdefghijkabcdefghijkabcdefghijk"), True)

    # def test_47(self):
    #     self.assertEqual(fn(s = "abcdefghijklmnopqrstuvwxyz", t = "bcdefghijklmnopqrstuvwxyza"), True)

    # def test_48(self):
    #     self.assertEqual(fn(s = "longlongstringwithvariouscharacters", t = "shortshort"), False)

    # def test_49(self):
    #     self.assertEqual(fn(s = "sos", t = "non"), True)

    # def test_50(self):
    #     self.assertEqual(fn(s = "rat", t = "car"), True)

    # def test_51(self):
    #     self.assertEqual(fn(s = "elephant", t = "mouse"), False)

    # def test_52(self):
    #     self.assertEqual(fn(s = "abc", t = "zyx"), True)

    # def test_53(self):
    #     self.assertEqual(fn(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz", t = "zzxxwwvvuuttssrrqqppoonnmmllkkjjiihhggeeffddccbbaa"), True)

    # def test_54(self):
    #     self.assertEqual(fn(s = "isomorphic", t = "esomoprphc"), False)

    # def test_55(self):
    #     self.assertEqual(fn(s = "aaabbbccc", t = "xxxyyyzzz"), True)

    # def test_56(self):
    #     self.assertEqual(fn(s = "abcdefghij", t = "jihgfedcba"), True)

    # def test_57(self):
    #     self.assertEqual(fn(s = "aaaaaa", t = "bbbbbb"), True)

    # def test_58(self):
    #     self.assertEqual(fn(s = "mississippi", t = "bbcccb"), False)

    # def test_59(self):
    #     self.assertEqual(fn(s = "xyxxyxyxyx", t = "xyxyyxyxyx"), False)

    # def test_60(self):
    #     self.assertEqual(fn(s = "aaaabbbbccccdddd", t = "ddddccccbbbbaaaa"), True)

    # # def test_61(self):
    # #     self.assertEqual(fn(s = "a!b@c#d$e%f^g&h*i(j)k_l+m-n=o[p]q{r}s|t\u'v"w"x"y"z", t = "z"y"x"w"v'u\t|s{r}q[p]o=n-m_l)k*i&h^f$e#d@c!b"), Error: Solution.isIsomorphic() missing 2 required positional arguments: 's' and 't')

    # def test_62(self):
    #     self.assertEqual(fn(s = "sameexample", t = "gnatgnatgnat"), False)

    # def test_63(self):
    #     self.assertEqual(fn(s = "twosky", t = "threesky"), False)

    # def test_64(self):
    #     self.assertEqual(fn(s = "abcabcabc", t = "xyzxyzxyz"), True)

    # def test_65(self):
    #     self.assertEqual(fn(s = "hellohello", t = "worldworld"), False)

    # def test_66(self):
    #     self.assertEqual(fn(s = "12345", t = "54321"), True)

    # def test_67(self):
    #     self.assertEqual(fn(s = "aabbccddeeffgghhii", t = "zzxxyywwvvuuttrrqqpp"), True)

    # def test_68(self):
    #     self.assertEqual(fn(s = "123123123", t = "abcabcabc"), True)

    # def test_69(self):
    #     self.assertEqual(fn(s = "racecar", t = "level"), False)

    # def test_70(self):
    #     self.assertEqual(fn(s = "racecar", t = "madam"), False)

    # def test_71(self):
    #     self.assertEqual(fn(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz", t = "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa"), True)

    # def test_72(self):
    #     self.assertEqual(fn(s = "abacabadabacaba", t = "xyxyxyxyxyxyxyxy"), False)

    # def test_73(self):
    #     self.assertEqual(fn(s = "abcdeffedcba", t = "gfedcbaabcdefg"), False)

    # def test_74(self):
    #     self.assertEqual(fn(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz", t = "zzyyxxwwvvuuttrrssqqppoonnmmllkkjjiihhggeeffdccbbbaa"), False)

    # def test_75(self):
    #     self.assertEqual(fn(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz", t = "zzzzyyyxxwwvvuuttrrsqqppoonnmmllkkjjiihhggffeeddccbbaa"), False)

    # def test_76(self):
    #     self.assertEqual(fn(s = "1234567890", t = "!@#$%^&*()"), True)

    # def test_77(self):
    #     self.assertEqual(fn(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz", t = "zzxxwvuttssrrqqponmlkjihgfedcbbaa"), False)

    # def test_78(self):
    #     self.assertEqual(fn(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz", t = "zzyyxxwwvvuuttrrssqqppoonnmmllkkjjiihhhgggffeeeeddccbbbaa"), False)

    # def test_79(self):
    #     self.assertEqual(fn(s = "xyzzxyzz", t = "abccabcc"), True)

    # def test_80(self):
    #     self.assertEqual(fn(s = "abcdefghijklmnopqrstuvwxyz", t = "abcdefghijklmnopqrstuvwxyz"), True)

    # def test_81(self):
    #     self.assertEqual(fn(s = "thisisatest", t = "abccbaabcab"), False)

    # def test_82(self):
    #     self.assertEqual(fn(s = "abcdabcdabcdabcd", t = "dcbaabcdabcdabcd"), False)

    # def test_83(self):
    #     self.assertEqual(fn(s = "anagram", t = "nagaram"), False)

    # def test_84(self):
    #     self.assertEqual(fn(s = "aaaaabbbbbccccc", t = "bbbbbcccccaaaaa"), True)

    # def test_85(self):
    #     self.assertEqual(fn(s = "abcdabcd", t = "wxyzwxyz"), True)

    # def test_86(self):
    #     self.assertEqual(fn(s = "twowords", t = "twooorld"), False)

    # def test_87(self):
    #     self.assertEqual(fn(s = "abbabbbbabaabababbaaabbbabbbaaa", t = "xyzxxzzxzyzyzyzyzyzyzyzyzyzyzyzyzyz"), False)

    # def test_88(self):
    #     self.assertEqual(fn(s = "aaabbbcccdddeeefffggghhhh", t = "mmmnnnoooqqrssstttuuuvvvvv"), False)

    # def test_89(self):
    #     self.assertEqual(fn(s = "mississippi", t = "bbjjjjbbbrrr"), False)

    # def test_90(self):
    #     self.assertEqual(fn(s = "abab", t = "baba"), True)

    # def test_91(self):
    #     self.assertEqual(fn(s = "thisisatest", t = "thisisatest"), True)

    # def test_92(self):
    #     self.assertEqual(fn(s = "unique", t = "unique"), True)

    # def test_93(self):
    #     self.assertEqual(fn(s = "abcabcabcabc", t = "defgdefgdefgdefg"), False)

    # def test_94(self):
    #     self.assertEqual(fn(s = "isomorphic", t = "homomorphi"), False)

    # def test_95(self):
    #     self.assertEqual(fn(s = "aaaaabbbbbaaaa", t = "cccceeeedddd"), False)

    # def test_96(self):
    #     self.assertEqual(fn(s = "xxxxx", t = "yyyyy"), True)

    # def test_97(self):
    #     self.assertEqual(fn(s = "abcabcabcabc", t = "xyzxyzxyzxyz"), True)

    # def test_98(self):
    #     self.assertEqual(fn(s = "abcabcabc", t = "xyzxyzyxzy"), False)

    # def test_99(self):
    #     self.assertEqual(fn(s = "isomorphic", t = "homomorphic"), False)

    # def test_100(self):
    #     self.assertEqual(fn(s = "sabcsabc", t = "tabctabc"), True)

    # def test_101(self):
    #     self.assertEqual(fn(s = "qwertyuiopasdfghjklzxcvbnm", t = "mlkjihgfdsapoiuytrewqzxcvbnm"), False)

    # def test_102(self):
    #     self.assertEqual(fn(s = "thisisatest", t = "thatistest"), False)

    # def test_103(self):
    #     self.assertEqual(fn(s = "!@#$%^&*()", t = "()&*^%$#@!"), True)

    # def test_104(self):
    #     self.assertEqual(fn(s = "racecar", t = "kayyak"), False)

    # def test_105(self):
    #     self.assertEqual(fn(s = "!@#$%^&*()", t = ")(*&^%$#@!"), True)

    # def test_106(self):
    #     self.assertEqual(fn(s = "sphinxofblackquartzjumps", t = "zpmxkbvhnckgyusldqpj"), False)

    # def test_107(self):
    #     self.assertEqual(fn(s = "1122334455", t = "1122334455"), True)

    # def test_108(self):
    #     self.assertEqual(fn(s = "ab", t = "zy"), True)

    # def test_109(self):
    #     self.assertEqual(fn(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz", t = "zzxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa"), True)

    # def test_110(self):
    #     self.assertEqual(fn(s = "aaaaaa", t = "zzzzzz"), True)

    # def test_111(self):
    #     self.assertEqual(fn(s = "noon", t = "moon"), False)

    # def test_112(self):
    #     self.assertEqual(fn(s = "aaaaabbbbccccddddd", t = "bbbbbccccdddddfffff"), False)

    # def test_113(self):
    #     self.assertEqual(fn(s = "special$chars!@#", t = "normal%^&*()"), False)

    # def test_114(self):
    #     self.assertEqual(fn(s = "abcabcabcabc", t = "defdefdefdef"), True)

    # def test_115(self):
    #     self.assertEqual(fn(s = "mississippi", t = "bbnnnnoooppp"), False)

    # def test_116(self):
    #     self.assertEqual(fn(s = "teest", t = "beest"), False)

    # def test_117(self):
    #     self.assertEqual(fn(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz", t = "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba"), True)

    # def test_118(self):
    #     self.assertEqual(fn(s = "!@#$%^", t = "^%$#@!"), True)

    # def test_119(self):
    #     self.assertEqual(fn(s = "unique", t = "mapped"), False)

    # def test_120(self):
    #     self.assertEqual(fn(s = "mississippi", t = "eeffgghhiiii"), False)

    # def test_121(self):
    #     self.assertEqual(fn(s = "xyxxyxyxyx", t = "zvzvzvzvzv"), False)

    # def test_122(self):
    #     self.assertEqual(fn(s = "abacabadabacaba", t = "xyxzyxzyzxzyxzy"), False)

    # def test_123(self):
    #     self.assertEqual(fn(s = "aabbccddeeffgghhiijj", t = "zzxxccvvnnooppmmqqllkk"), True)

    # def test_124(self):
    #     self.assertEqual(fn(s = "abababab", t = "cdcdcdcd"), True)

    # def test_125(self):
    #     self.assertEqual(fn(s = "xyxzyzyx", t = "qpqpqpqp"), False)

    # def test_126(self):
    #     self.assertEqual(fn(s = "abcdefghijabcdefghij", t = "klmnopqrstklmnopqrst"), True)

    # def test_127(self):
    #     self.assertEqual(fn(s = "aabbccddeeff", t = "zzxxyywwvvuutt"), True)

    # def test_128(self):
    #     self.assertEqual(fn(s = "elephant", t = "zuluqaak"), False)

    # def test_129(self):
    #     self.assertEqual(fn(s = "mississippi", t = "lllssssiiip"), False)

    # def test_130(self):
    #     self.assertEqual(fn(s = "thisproblemisfun", t = "thatquestionistame"), False)

    # def test_131(self):
    #     self.assertEqual(fn(s = "abcdefghij", t = "abcdefghij"), True)
