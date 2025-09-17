import unittest
from solution_find_the_index_of_the_first_occurrence_in_a_string import Solution

fn = Solution().strStr

class Test(unittest.TestCase):

    def test_0(self):
        self.assertEqual(fn(haystack = "ababcabcabababd", needle = "ababd"), 10)

    def test_1(self):
        self.assertEqual(fn(haystack = "abcde", needle = "f"), -1)

    def test_2(self):
        self.assertEqual(fn(haystack = "mississippi", needle = "issi"), 1)

    def test_3(self):
        self.assertEqual(fn(haystack = "sadbutsad", needle = "sad"), 0)

    def test_4(self):
        self.assertEqual(fn(haystack = "abababa", needle = "aba"), 0)

    def test_5(self):
        self.assertEqual(fn(haystack = "abcdefgh", needle = "efg"), 4)

    def test_6(self):
        self.assertEqual(fn(haystack = "abc", needle = "c"), 2)

    def test_7(self):
        self.assertEqual(fn(haystack = "aaaaa", needle = "bba"), -1)

    def test_8(self):
        self.assertEqual(fn(haystack = "mississippi", needle = "issip"), 4)

    def test_9(self):
        self.assertEqual(fn(haystack = "abc", needle = "d"), -1)

    def test_10(self):
        self.assertEqual(fn(haystack = "a", needle = "a"), 0)

    def test_11(self):
        self.assertEqual(fn(haystack = "hello", needle = "ll"), 2)

    def test_12(self):
        self.assertEqual(fn(haystack = "leetcode", needle = "leeto"), -1)

    def test_13(self):
        self.assertEqual(fn(haystack = "ababababab", needle = "aba"), 0)

    def test_14(self):
        self.assertEqual(fn(haystack = "randomrandomrandom", needle = "random"), 0)

    def test_15(self):
        self.assertEqual(fn(haystack = "abcdefgabcdefgabcdefg", needle = "efg"), 4)

    def test_16(self):
        self.assertEqual(fn(haystack = "abcdefg", needle = ""), 0)

    def test_17(self):
        self.assertEqual(fn(haystack = "a quick brown fox jumps over the lazy dog", needle = "quack"), -1)

    def test_18(self):
        self.assertEqual(fn(haystack = "abracadabra", needle = "cad"), 4)

    def test_19(self):
        self.assertEqual(fn(haystack = "aaaaaaabc", needle = "aaaaaab"), 1)

    def test_20(self):
        self.assertEqual(fn(haystack = "level", needle = "eve"), 1)

    def test_21(self):
        self.assertEqual(fn(haystack = "aaaaaa", needle = "aaa"), 0)

    def test_22(self):
        self.assertEqual(fn(haystack = "abababab", needle = "aba"), 0)

    def test_23(self):
        self.assertEqual(fn(haystack = "abcde", needle = ""), 0)

    def test_24(self):
        self.assertEqual(fn(haystack = "xylophone", needle = "phone"), 4)

    def test_25(self):
        self.assertEqual(fn(haystack = "abcdeabcdeabcde", needle = "deabc"), 3)

    def test_26(self):
        self.assertEqual(fn(haystack = "quickbrownfox", needle = "quick"), 0)

    def test_27(self):
        self.assertEqual(fn(haystack = "repeatedstringrepeatedstring", needle = "string"), 8)

    def test_28(self):
        self.assertEqual(fn(haystack = "abcde", needle = "abcde"), 0)

    def test_29(self):
        self.assertEqual(fn(haystack = "noinneedlehere", needle = "needle"), 4)

    def test_30(self):
        self.assertEqual(fn(haystack = "banana", needle = "ana"), 1)

    def test_31(self):
        self.assertEqual(fn(haystack = "abcdefghijklmnopqrstuvwxyz", needle = "mnop"), 12)

    def test_32(self):
        self.assertEqual(fn(haystack = "abcabcabcabcabcabc", needle = "abcabc"), 0)

    def test_33(self):
        self.assertEqual(fn(haystack = "boundarycase", needle = "boundarycase"), 0)

    def test_34(self):
        self.assertEqual(fn(haystack = "abcabcabcabc", needle = "bcabc"), 1)

    def test_35(self):
        self.assertEqual(fn(haystack = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz", needle = "mnopqrstuv"), -1)

    def test_36(self):
        self.assertEqual(fn(haystack = "sequence", needle = "qu"), 2)

    def test_37(self):
        self.assertEqual(fn(haystack = "bananananana", needle = "nan"), 2)

    def test_38(self):
        self.assertEqual(fn(haystack = "aaaaaaaaaaaaaaaaaa", needle = "aaaaaaaaaa"), 0)

    def test_39(self):
        self.assertEqual(fn(haystack = "abcdefghij", needle = "jihgfedcba"), -1)

    def test_40(self):
        self.assertEqual(fn(haystack = "abcdefghij", needle = "abcdefghij"), 0)

    def test_41(self):
        self.assertEqual(fn(haystack = "thisisaverylongstringwithsomecharacters", needle = "characters"), 29)

    def test_42(self):
        self.assertEqual(fn(haystack = "thisisaverylongstringwithsomerepeatingpatterns", needle = "patterns"), 38)

    def test_43(self):
        self.assertEqual(fn(haystack = "thesamethesame", needle = "thesame"), 0)

    def test_44(self):
        self.assertEqual(fn(haystack = "noon", needle = "noon"), 0)

    def test_45(self):
        self.assertEqual(fn(haystack = "hellohellohellohellohello", needle = "hellohello"), 0)

    def test_46(self):
        self.assertEqual(fn(haystack = "nnnnnnnnnn", needle = "nnnn"), 0)

    def test_47(self):
        self.assertEqual(fn(haystack = "12345678901234567890", needle = "56789012"), 4)

    def test_48(self):
        self.assertEqual(fn(haystack = "12345678901234567890", needle = "56789"), 4)

    def test_49(self):
        self.assertEqual(fn(haystack = "abcabcabcabcabc", needle = "cab"), 2)

    def test_50(self):
        self.assertEqual(fn(haystack = "thisisaverylonghaystack", needle = "averylong"), 6)

    def test_51(self):
        self.assertEqual(fn(haystack = "hellohellohello", needle = "hellohello"), 0)

    def test_52(self):
        self.assertEqual(fn(haystack = "singleletter", needle = "a"), -1)

    def test_53(self):
        self.assertEqual(fn(haystack = "oneonetwoonethreeonethreeone", needle = "three"), 12)

    def test_54(self):
        self.assertEqual(fn(haystack = "abcabcabcabcabcabc", needle = "cab"), 2)

    def test_55(self):
        self.assertEqual(fn(haystack = "pythonprogrammingpython", needle = "thonpro"), 2)

    def test_56(self):
        self.assertEqual(fn(haystack = "repeatedcharactersequenceeeeeeeeeeeeeee", needle = "eeeeeeee"), 24)

    def test_57(self):
        self.assertEqual(fn(haystack = "abcdabcyabcdabc", needle = "abcdabc"), 0)

    def test_58(self):
        self.assertEqual(fn(haystack = "mississippi", needle = "issipp"), 4)

    def test_59(self):
        self.assertEqual(fn(haystack = "aaaaabaaaabaaaaabaaaabaaaaabaaaabaaaaabaaaab", needle = "baaab"), -1)

    def test_60(self):
        self.assertEqual(fn(haystack = "aaaaaa", needle = "aaaaaaa"), -1)

    def test_61(self):
        self.assertEqual(fn(haystack = "abcdefghijklmnopqrstuvwxyz", needle = "xyz"), 23)

    def test_62(self):
        self.assertEqual(fn(haystack = "overlaplaplaplaplap", needle = "lap"), 4)

    def test_63(self):
        self.assertEqual(fn(haystack = "aaaaabaaaaaa", needle = "aaaaab"), 0)

    def test_64(self):
        self.assertEqual(fn(haystack = "helloworldhelloworld", needle = "worldhello"), 5)

    def test_65(self):
        self.assertEqual(fn(haystack = "abracadabra", needle = "abra"), 0)

    def test_66(self):
        self.assertEqual(fn(haystack = "abababababababababab", needle = "ababab"), 0)

    def test_67(self):
        self.assertEqual(fn(haystack = "aabbccddeeffgghhiijjkk", needle = "eeffgg"), 8)

    def test_68(self):
        self.assertEqual(fn(haystack = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz", needle = "mnop"), -1)

    def test_69(self):
        self.assertEqual(fn(haystack = "mississippiissippi", needle = "issip"), 4)

    def test_70(self):
        self.assertEqual(fn(haystack = "aquickbrownfoxjumpsoverthelazydog", needle = "dog"), 30)

    def test_71(self):
        self.assertEqual(fn(haystack = "abababababababab", needle = "ababab"), 0)

    def test_72(self):
        self.assertEqual(fn(haystack = "almostsameprefixalmost", needle = "almost"), 0)

    def test_73(self):
        self.assertEqual(fn(haystack = "qwertyuiopasdfghjklzxcvbnm", needle = "qwertyuiop"), 0)

    def test_74(self):
        self.assertEqual(fn(haystack = "ananananananan", needle = "anana"), 0)

    def test_75(self):
        self.assertEqual(fn(haystack = "averylongstringwithrepeatedcharactersaaaaaaaaa", needle = "aaaaaaaa"), 37)

    def test_76(self):
        self.assertEqual(fn(haystack = "", needle = ""), 0)

    def test_77(self):
        self.assertEqual(fn(haystack = "findinganoccurrenceinanarray", needle = "anoccurrence"), 7)

    def test_78(self):
        self.assertEqual(fn(haystack = "repeatedrepeatedrepeated", needle = "repeated"), 0)

    def test_79(self):
        self.assertEqual(fn(haystack = "pythonprogramming", needle = "programming"), 6)

    def test_80(self):
        self.assertEqual(fn(haystack = "palindrome", needle = "alin"), 1)

    def test_81(self):
        self.assertEqual(fn(haystack = "singleletter", needle = "s"), 0)

    def test_82(self):
        self.assertEqual(fn(haystack = "aaaaaabaaaaaab", needle = "aaaaaab"), 0)

    def test_83(self):
        self.assertEqual(fn(haystack = "thisisaverylongstringthatwilltestouralgorithm", needle = "longstring"), 11)

    def test_84(self):
        self.assertEqual(fn(haystack = "this is a simple test", needle = "simple"), 10)

    def test_85(self):
        self.assertEqual(fn(haystack = "aaaaabaaaabaaaaabaaaab", needle = "aaaab"), 1)

    def test_86(self):
        self.assertEqual(fn(haystack = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz", needle = "zzzzzzzzzz"), 0)

    def test_87(self):
        self.assertEqual(fn(haystack = "repeatedrepeatedrepeated", needle = "repeatedre"), 0)

    def test_88(self):
        self.assertEqual(fn(haystack = "thelastwordisneedle", needle = "needle"), 13)

    def test_89(self):
        self.assertEqual(fn(haystack = "hellohellohello", needle = "lohe"), 3)

    def test_90(self):
        self.assertEqual(fn(haystack = "abababababab", needle = "ababab"), 0)

    def test_91(self):
        self.assertEqual(fn(haystack = "abababababab", needle = "bababa"), 1)

    def test_92(self):
        self.assertEqual(fn(haystack = "thisisaverylongstringforatest", needle = "avery"), 6)

    def test_93(self):
        self.assertEqual(fn(haystack = "overlappingoverlap", needle = "lapping"), 4)

    def test_94(self):
        self.assertEqual(fn(haystack = "findthehiddenpattern", needle = "hidden"), 7)

    def test_95(self):
        self.assertEqual(fn(haystack = "ababababab", needle = "abab"), 0)

    def test_96(self):
        self.assertEqual(fn(haystack = "asubstringrightattheend", needle = "end"), 20)

    def test_97(self):
        self.assertEqual(fn(haystack = "longstringthatcontainsavarietyofcharacters", needle = "characters"), 32)

    def test_98(self):
        self.assertEqual(fn(haystack = "bananaanabanana", needle = "anaban"), 6)

    def test_99(self):
        self.assertEqual(fn(haystack = "racecar", needle = "race"), 0)

    def test_100(self):
        self.assertEqual(fn(haystack = "longstringwithnokeyword", needle = "keyword"), 16)

    def test_101(self):
        self.assertEqual(fn(haystack = "abcdefghij", needle = "gh"), 6)

    def test_102(self):
        self.assertEqual(fn(haystack = "mississippi", needle = "pi"), 9)

    def test_103(self):
        self.assertEqual(fn(haystack = "verylonghaystackwithrepeatingcharactersaaaaaaaaaaa", needle = "aaaaa"), 39)

    def test_104(self):
        self.assertEqual(fn(haystack = "", needle = "a"), -1)

    def test_105(self):
        self.assertEqual(fn(haystack = "a", needle = ""), 0)

    def test_106(self):
        self.assertEqual(fn(haystack = "09876543210987654321", needle = "654321"), 4)

    def test_107(self):
        self.assertEqual(fn(haystack = "hellohellohello", needle = "hello"), 0)

    def test_108(self):
        self.assertEqual(fn(haystack = "aaaaaaaaaaa", needle = "aaaaaa"), 0)

    def test_109(self):
        self.assertEqual(fn(haystack = "thisisaverylongstringthatcontainsmultiplesubstrings", needle = "substring"), 41)

    def test_110(self):
        self.assertEqual(fn(haystack = "uniquecharacters", needle = "characters"), 6)

    def test_111(self):
        self.assertEqual(fn(haystack = "aaaaaaab", needle = "aaaab"), 3)

    def test_112(self):
        self.assertEqual(fn(haystack = "almosttherealmost", needle = "almostthere"), 0)

    def test_113(self):
        self.assertEqual(fn(haystack = "aaaaaaaaaab", needle = "aaaaaab"), 4)

    def test_114(self):
        self.assertEqual(fn(haystack = "aaaaabaaaaabaaaaab", needle = "aaaaab"), 0)

    def test_115(self):
        self.assertEqual(fn(haystack = "a quick brown fox jumps over the lazy dog", needle = "quick"), 2)

    def test_116(self):
        self.assertEqual(fn(haystack = "thisisaverylongstringwithrepeatedpatterns", needle = "repeated"), 25)

    def test_117(self):
        self.assertEqual(fn(haystack = "thisisaverylonghaystackthatcontainsavariablesubstring", needle = "substring"), 44)

    def test_118(self):
        self.assertEqual(fn(haystack = "xxyyzzxxyyzzxxyyzz", needle = "xxyyzz"), 0)

    def test_119(self):
        self.assertEqual(fn(haystack = "aaaaa", needle = "aa"), 0)

    def test_120(self):
        self.assertEqual(fn(haystack = "ababababababababa", needle = "abab"), 0)

    def test_121(self):
        self.assertEqual(fn(haystack = "a quick brown fox jumps over the lazy dog", needle = "lazy"), 33)

    def test_122(self):
        self.assertEqual(fn(haystack = "needleinthestack", needle = "needle"), 0)

    def test_123(self):
        self.assertEqual(fn(haystack = "aaaaaaaaaaaaaaaaaaaa", needle = "aaaaaaaaa"), 0)

    def test_124(self):
        self.assertEqual(fn(haystack = "aaaaaaab", needle = "aaaaaab"), 1)

    def test_125(self):
        self.assertEqual(fn(haystack = "aaaa", needle = "aaaaa"), -1)

    def test_126(self):
        self.assertEqual(fn(haystack = "substring", needle = "string"), 3)

    def test_127(self):
        self.assertEqual(fn(haystack = "xyzxyzxyzxyz", needle = "zyx"), -1)

    def test_128(self):
        self.assertEqual(fn(haystack = "abababababababababab", needle = "abab"), 0)

    def test_129(self):
        self.assertEqual(fn(haystack = "oneonetwoonetwothree", needle = "twone"), -1)

    def test_130(self):
        self.assertEqual(fn(haystack = "bananananana", needle = "anan"), 1)

    def test_131(self):
        self.assertEqual(fn(haystack = "xyxxyxyxyxyxyxyx", needle = "xyxyx"), 3)

    def test_132(self):
        self.assertEqual(fn(haystack = "aaaaabaaaa", needle = "aaab"), 2)

    def test_133(self):
        self.assertEqual(fn(haystack = "abcdefghij", needle = "efgh"), 4)

    def test_134(self):
        self.assertEqual(fn(haystack = "overlaplaplaplap", needle = "laplap"), 4)

    def test_135(self):
        self.assertEqual(fn(haystack = "thisisaverylongstringforsearching", needle = "searching"), 24)

    def test_136(self):
        self.assertEqual(fn(haystack = "bananabananabanana", needle = "nan"), 2)

    def test_137(self):
        self.assertEqual(fn(haystack = "longhaystackwithaveryspecificsubstring", needle = "averyspecific"), 16)

    def test_138(self):
        self.assertEqual(fn(haystack = "aaaaaaa", needle = "aaaaaa"), 0)

    def test_139(self):
        self.assertEqual(fn(haystack = "abcdefabcdefabcdefabcdef", needle = "cdef"), 2)

    def test_140(self):
        self.assertEqual(fn(haystack = "aaaaabaaaaabaaaaabaaaaab", needle = "aaaab"), 1)

    def test_141(self):
        self.assertEqual(fn(haystack = "hellohellohello", needle = "lohel"), 3)

    def test_142(self):
        self.assertEqual(fn(haystack = "abcdabcdabcd", needle = "cdab"), 2)

    def test_143(self):
        self.assertEqual(fn(haystack = "banana", needle = "na"), 2)
