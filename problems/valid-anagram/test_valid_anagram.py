import unittest
from solution_valid_anagram import Solution

fn = Solution().isAnagram

class Test(unittest.TestCase):

    def test_0(self):
        self.assertEqual(fn(s = "abcdefghijklmnopqrstuvwxyz", t = "zyxwvutsrqponmlkjihgfedcba"), True)

    def test_1(self):
        self.assertEqual(fn(s = "abcde", t = "edcba"), True)

    def test_2(self):
        self.assertEqual(fn(s = "abc", t = "abcd"), False)

    def test_3(self):
        self.assertEqual(fn(s = "apple", t = "pale"), False)

    def test_4(self):
        self.assertEqual(fn(s = "hello", t = "bello"), False)

    def test_5(self):
        self.assertEqual(fn(s = "aacc", t = "ccac"), False)

    def test_6(self):
        self.assertEqual(fn(s = "abc", t = "def"), False)

    def test_7(self):
        self.assertEqual(fn(s = "abc", t = "cba"), True)

    def test_8(self):
        self.assertEqual(fn(s = "abcd", t = "abce"), False)

    def test_9(self):
        self.assertEqual(fn(s = "anagram", t = "nagaram"), True)

    def test_10(self):
        self.assertEqual(fn(s = "rat", t = "car"), False)

    def test_11(self):
        self.assertEqual(fn(s = "a", t = "a"), True)

    def test_12(self):
        self.assertEqual(fn(s = "ab", t = "ba"), True)

    def test_13(self):
        self.assertEqual(fn(s = "listen", t = "silent"), True)

    def test_14(self):
        self.assertEqual(fn(s = "abcd", t = "dcba"), True)

    def test_15(self):
        self.assertEqual(fn(s = "triangle", t = "integral"), True)

    def test_16(self):
        self.assertEqual(fn(s = "aabbcc", t = "abcabc"), True)

    def test_17(self):
        self.assertEqual(fn(s = "", t = ""), True)

    def test_18(self):
        self.assertEqual(fn(s = "ababababababababab", t = "bababababababababa"), True)

    def test_19(self):
        self.assertEqual(fn(s = "hello world", t = "worldhello"), False)

    def test_20(self):
        self.assertEqual(fn(s = "theeyes", t = "theysee"), True)

    # def test_21(self):
    #     self.assertEqual(fn(s = "a" * 50000, t = "a" * 50000), Error: Solution.isAnagram() missing 2 required positional arguments: 's' and 't')

    def test_22(self):
        self.assertEqual(fn(s = "repeatedcharactershere", t = "repeatedcharactershere"), True)

    def test_23(self):
        self.assertEqual(fn(s = "ababababab", t = "bababababa"), True)

    def test_24(self):
        self.assertEqual(fn(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz", t = "zzxxyywwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa"), True)

    def test_25(self):
        self.assertEqual(fn(s = "the quick brown fox", t = "xof nworb kciuq eht"), True)

    def test_26(self):
        self.assertEqual(fn(s = "astronomer", t = "moonstarer"), True)

    def test_27(self):
        self.assertEqual(fn(s = "thisisananagram", t = "isanagramthis"), False)

    def test_28(self):
        self.assertEqual(fn(s = "spaces should be ignored", t = "should be ignored spaces"), True)

    def test_29(self):
        self.assertEqual(fn(s = "aabbcc", t = "ccbbaa"), True)

    def test_30(self):
        self.assertEqual(fn(s = "special!@#$%^&*()characters", t = "characters)!@#$%^&*()special"), False)

    def test_31(self):
        self.assertEqual(fn(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz", t = "zzzzyyyxxxwwwwvvvvuuuuttttssssrrrrqqqqppppooooonnnnmmmmllllkkkkjjjjiiiigggghhhhffffffeeeeeeeeddccccbbbbaaaa"), False)

    def test_32(self):
        self.assertEqual(fn(s = "anagram", t = "nagarams"), False)

    def test_33(self):
        self.assertEqual(fn(s = "dormitory", t = "dirtyroom"), True)

    def test_34(self):
        self.assertEqual(fn(s = "1234567890", t = "0987654321"), True)

    def test_35(self):
        self.assertEqual(fn(s = "anananana", t = "naanaanna"), True)

    def test_36(self):
        self.assertEqual(fn(s = "", t = "a"), False)

    def test_37(self):
        self.assertEqual(fn(s = "thisisanagramtest", t = "agamnartisiesttst"), False)

    def test_38(self):
        self.assertEqual(fn(s = "hello world", t = "world hello"), True)

    def test_39(self):
        self.assertEqual(fn(s = "a gentleman", t = "elegant man"), True)

    def test_40(self):
        self.assertEqual(fn(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz", t = "zzyyxxwwvvuuttrrssqqppoonnmmllkkjjiihhggffeeddccbbaa"), True)

    def test_41(self):
        self.assertEqual(fn(s = "aabbcc", t = "aabbc"), False)

    # def test_42(self):
    #     self.assertEqual(fn(s = "b" * 50000, t = "a" * 50000), Error: Solution.isAnagram() missing 2 required positional arguments: 's' and 't')

    def test_43(self):
        self.assertEqual(fn(s = "school master", t = "the classroom"), True)

    def test_44(self):
        self.assertEqual(fn(s = "thisisaverylongstringthatwearetesting", t = "averylongstringthatwearetestingthisis"), True)

    # def test_45(self):
    #     self.assertEqual(fn(s = "a" * 50000, t = "a" * 49999 + "b"), Error: Solution.isAnagram() missing 2 required positional arguments: 's' and 't')

    def test_46(self):
        self.assertEqual(fn(s = "thequickbrownfoxjumpsoverthelazydog", t = "godzylathedelvropmusfixnworbquickthe"), False)

    def test_47(self):
        self.assertEqual(fn(s = "thisisananagram", t = "isananagramthis"), True)

    def test_48(self):
        self.assertEqual(fn(s = "funeral", t = "real fun"), False)

    def test_49(self):
        self.assertEqual(fn(s = "unitedstates", t = "adtenisestatesu"), False)

    def test_50(self):
        self.assertEqual(fn(s = "mississippi", t = "mississipi"), False)

    # def test_51(self):
    #     self.assertEqual(fn(s = "a" * 25000 + "b" * 25000, t = "b" * 25000 + "a" * 25000), Error: Solution.isAnagram() missing 2 required positional arguments: 's' and 't')

    def test_52(self):
        self.assertEqual(fn(s = "elevenplus", t = "twelvestop"), False)

    def test_53(self):
        self.assertEqual(fn(s = "a", t = "b"), False)

    def test_54(self):
        self.assertEqual(fn(s = "anagramanagramanagram", t = "nagaramnagaramnagaram"), True)

    def test_55(self):
        self.assertEqual(fn(s = "aabbccdd", t = "ddbbaacc"), True)

    def test_56(self):
        self.assertEqual(fn(s = "aquickbrownfoxjumpsoverthelazydog", t = "quickbrownfoxjumpsoverthelazydoga"), True)

    def test_57(self):
        self.assertEqual(fn(s = "abcdeabced", t = "abcedabcde"), True)

    def test_58(self):
        self.assertEqual(fn(s = "aquickbrownfoxjumpsoverthelazydog", t = "thelazydogjumpsoveraquickbrownfox"), True)

    def test_59(self):
        self.assertEqual(fn(s = "pythonprogramming", t = "nohtypgnimmargorp"), True)

    def test_60(self):
        self.assertEqual(fn(s = "forty five", t = "over fifty"), True)

    def test_61(self):
        self.assertEqual(fn(s = "a!@#b$%^c&*()", t = "c&*()b$%^a!@#"), True)

    def test_62(self):
        self.assertEqual(fn(s = "aquickbrownfoxjumpsoverthelazydog", t = "quickbrownfoxjumpsoverthelazygod"), False)

    def test_63(self):
        self.assertEqual(fn(s = "noon", t = "noon"), True)

    def test_64(self):
        self.assertEqual(fn(s = "anagrammatic", t = "icnagarammat"), True)

    def test_65(self):
        self.assertEqual(fn(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz", t = "zyxwvutsrqponmlkjihgfedcba"), False)

    def test_66(self):
        self.assertEqual(fn(s = "abacabadabacaba", t = "bacabacabacaba"), False)

    def test_67(self):
        self.assertEqual(fn(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz", t = "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggeeffddeebbaa"), False)

    def test_68(self):
        self.assertEqual(fn(s = "the quick brown fox jumps over the lazy dog", t = "dog lazy the over jumps fox brown quick the"), True)

    def test_69(self):
        self.assertEqual(fn(s = "conversation", t = "voices rant on"), False)

    def test_70(self):
        self.assertEqual(fn(s = "eleven plus two", t = "twelve plus one"), True)

    def test_71(self):
        self.assertEqual(fn(s = "the eyes", t = "they see"), True)

    # def test_72(self):
    #     self.assertEqual(fn(s = "a" * 50000 + "b", t = "a" * 50000), Error: Solution.isAnagram() missing 2 required positional arguments: 's' and 't')

    def test_73(self):
        self.assertEqual(fn(s = "conversation", t = "voicesranton"), True)

    def test_74(self):
        self.assertEqual(fn(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz", t = "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggeeffddccbbbaa"), False)

    def test_75(self):
        self.assertEqual(fn(s = "anagramanagram", t = "nagaramnagaram"), True)

    # def test_76(self):
    #     self.assertEqual(fn(s = "a" * 49999 + "b", t = "a" * 50000), Error: Solution.isAnagram() missing 2 required positional arguments: 's' and 't')

    def test_77(self):
        self.assertEqual(fn(s = "this is a test", t = "test a is this"), True)

    def test_78(self):
        self.assertEqual(fn(s = "night", t = "thing"), True)

    def test_79(self):
        self.assertEqual(fn(s = "aaabbbccc", t = "bbbaaacc"), False)

    def test_80(self):
        self.assertEqual(fn(s = "samecharacters", t = "charactersames"), True)

    def test_81(self):
        self.assertEqual(fn(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz", t = "zzyxwvuttsrqponmlkjihgfeddcbaabbccddeeffgghhiijjkkllmmnnooppqqrrss"), False)

    def test_82(self):
        self.assertEqual(fn(s = "mississippi", t = "ssmissippii"), True)

    def test_83(self):
        self.assertEqual(fn(s = "abcabcabcabcabcabc", t = "abcabcabcabcabcabc"), True)

    def test_84(self):
        self.assertEqual(fn(s = "xxyyzz", t = "zzxxyy"), True)

    def test_85(self):
        self.assertEqual(fn(s = "thequickbrownfoxjumpsoverthelazydog", t = "thequickbrownfoxjumpsoverthelazygod"), True)

    def test_86(self):
        self.assertEqual(fn(s = "elevenpluszwo", t = "twelvezillion"), False)

    def test_87(self):
        self.assertEqual(fn(s = "notanagramhere", t = "anagramherenot"), True)

    def test_88(self):
        self.assertEqual(fn(s = "uniqueanagram", t = "nagramuniqueanagram"), False)

    def test_89(self):
        self.assertEqual(fn(s = "fluster", t = "restful"), True)

    def test_90(self):
        self.assertEqual(fn(s = "dormitory", t = "dirty room"), False)

    def test_91(self):
        self.assertEqual(fn(s = "aaaaaa", t = "aaaaa"), False)

    def test_92(self):
        self.assertEqual(fn(s = "punishments", t = "ninepunishment"), False)

    def test_93(self):
        self.assertEqual(fn(s = "thirty", t = "typhrirt"), False)

    def test_94(self):
        self.assertEqual(fn(s = "racecar", t = "carrace"), True)

    def test_95(self):
        self.assertEqual(fn(s = "ab", t = "aabb"), False)

    def test_96(self):
        self.assertEqual(fn(s = "a", t = ""), False)

    def test_97(self):
        self.assertEqual(fn(s = "qwertyuiopasdfghjklzxcvbnm", t = "mnbvcxzlkjhgfdsapoiuytrewq"), True)

    def test_98(self):
        self.assertEqual(fn(s = "abacax", t = "aacxab"), True)

    def test_99(self):
        self.assertEqual(fn(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz", t = "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba"), True)

    def test_100(self):
        self.assertEqual(fn(s = "questionnaire", t = "reinquirequest"), False)

    def test_101(self):
        self.assertEqual(fn(s = "anagramatically", t = "gramaticallyanagram"), False)

    def test_102(self):
        self.assertEqual(fn(s = "uniquecharacters", t = "uniquecharactersx"), False)

    def test_103(self):
        self.assertEqual(fn(s = "abcdabcdabcd", t = "dcbaabcdabcd"), True)

    def test_104(self):
        self.assertEqual(fn(s = "adobe", t = "abode"), True)

    def test_105(self):
        self.assertEqual(fn(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz", t = "zzzyyxwwvvuuttssrrqqppoonnmlkkjjiihhggffeeeeddccbaab"), False)

    def test_106(self):
        self.assertEqual(fn(s = "clint eastwood", t = "old west action"), False)

    def test_107(self):
        self.assertEqual(fn(s = "abcabcabcabc", t = "cbacbacbacba"), True)

    def test_108(self):
        self.assertEqual(fn(s = "schoolmaster", t = "theclassroom"), True)

    def test_109(self):
        self.assertEqual(fn(s = "embarrassing", t = "backgroundsere"), False)

    def test_110(self):
        self.assertEqual(fn(s = "racecar", t = "racecar"), True)

    def test_111(self):
        self.assertEqual(fn(s = "nematocysts", t = "cytoplasmnets"), False)

    def test_112(self):
        self.assertEqual(fn(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz", t = "zzyyxxwwvvuuttsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcbaa"), False)

    # def test_113(self):
    #     self.assertEqual(fn(s = "thequickbrownfoxjumpsoverthelazydog" * 1000, t = "godzylathedelvropmusfixnworbquickthe" * 1000), Error: Solution.isAnagram() missing 2 required positional arguments: 's' and 't')
