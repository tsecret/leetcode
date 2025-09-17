import unittest
from solution_merge_strings_alternately import Solution

fn = Solution().mergeAlternately

class Test(unittest.TestCase):

    def test_0(self):
        self.assertEqual(fn(word1 = "a", word2 = "b"), "ab")

    def test_1(self):
        self.assertEqual(fn(word1 = "abcd", word2 = "pq"), "apbqcd")

    def test_2(self):
        self.assertEqual(fn(word1 = "ab", word2 = "pqrs"), "apbqrs")

    def test_3(self):
        self.assertEqual(fn(word1 = "", word2 = "uvw"), "uvw")

    def test_4(self):
        self.assertEqual(fn(word1 = "x", word2 = "y"), "xy")

    def test_5(self):
        self.assertEqual(fn(word1 = "hello", word2 = "world"), "hweolrllod")

    # def test_6(self):
    #     self.assertEqual(fn(word1 = "a", word2 = "bcd"), abcd)

    # def test_7(self):
    #     self.assertEqual(fn(word1 = "abcde", word2 = "fgh"), afbgchde)

    # def test_8(self):
    #     self.assertEqual(fn(word1 = "abc", word2 = "pqr"), apbqcr)

    # def test_9(self):
    #     self.assertEqual(fn(word1 = "abcd", word2 = "e"), aebcd)

    # def test_10(self):
    #     self.assertEqual(fn(word1 = "xyz", word2 = ""), xyz)

    # def test_11(self):
    #     self.assertEqual(fn(word1 = "abcdefghijklmnopqrstuvwxyz", word2 = ""), abcdefghijklmnopqrstuvwxyz)

    # def test_12(self):
    #     self.assertEqual(fn(word1 = "a", word2 = "bcdefghijklmnopqrstuvwxyz"), abcdefghijklmnopqrstuvwxyz)

    # def test_13(self):
    #     self.assertEqual(fn(word1 = "thisisateststring", word2 = "anotheronehere"), tahniostihseartoensethsetrreing)

    # def test_14(self):
    #     self.assertEqual(fn(word1 = "aabbccdd", word2 = "eeffgg"), aeaebfbfcgcgdd)

    # def test_15(self):
    #     self.assertEqual(fn(word1 = "complex", word2 = "strings"), csotmrpilnegxs)

    # def test_16(self):
    #     self.assertEqual(fn(word1 = "xyz", word2 = "abcde"), xaybzcde)

    # def test_17(self):
    #     self.assertEqual(fn(word1 = "abcdefgh", word2 = "ijkl"), aibjckdlefgh)

    # def test_18(self):
    #     self.assertEqual(fn(word1 = "abcdefghijk", word2 = "lmnopqrstuvwxyz"), albmcndoepfqgrhsitjukvwxyz)

    # def test_19(self):
    #     self.assertEqual(fn(word1 = "abcdefghij", word2 = "klmnopqrstuvwxyz"), akblcmdneofpgqhrisjtuvwxyz)

    # def test_20(self):
    #     self.assertEqual(fn(word1 = "abcdefghijklmnopqrstuvwxy", word2 = "z"), azbcdefghijklmnopqrstuvwxy)

    # def test_21(self):
    #     self.assertEqual(fn(word1 = "quick", word2 = "brownfox"), qburiocwknfox)

    # def test_22(self):
    #     self.assertEqual(fn(word1 = "onetwothreefour", word2 = "five"), ofnievtewothreefour)

    # def test_23(self):
    #     self.assertEqual(fn(word1 = "overlap", word2 = "lapping"), olvaeprplianpg)

    # def test_24(self):
    #     self.assertEqual(fn(word1 = "", word2 = ""), )

    # def test_25(self):
    #     self.assertEqual(fn(word1 = "python", word2 = "java"), pjyatvhaon)

    # def test_26(self):
    #     self.assertEqual(fn(word1 = "abcdefgh", word2 = "ijklmnopqrstuv"), aibjckdlemfngohpqrstuv)

    # def test_27(self):
    #     self.assertEqual(fn(word1 = "different", word2 = "length"), dliefnfgetrhent)

    # def test_28(self):
    #     self.assertEqual(fn(word1 = "abcdefghij", word2 = "klmnopqrst"), akblcmdneofpgqhrisjt)

    # def test_29(self):
    #     self.assertEqual(fn(word1 = "abcdabcdabcd", word2 = "zyxwzyxwzyxw"), azbycxdwazbycxdwazbycxdw)

    # def test_30(self):
    #     self.assertEqual(fn(word1 = "longerfirstword", word2 = "short"), lsohnogretrfirstword)

    # def test_31(self):
    #     self.assertEqual(fn(word1 = "abcdefg", word2 = "hijklmnop"), ahbicjdkelfmgnop)

    # def test_32(self):
    #     self.assertEqual(fn(word1 = "abcdef", word2 = "ghijklmnopqrstuvwxyz"), agbhcidjekflmnopqrstuvwxyz)

    # def test_33(self):
    #     self.assertEqual(fn(word1 = "xyz", word2 = "abcdefg"), xaybzcdefg)

    # def test_34(self):
    #     self.assertEqual(fn(word1 = "abcdabcdabcd", word2 = "efghefghefghefgh"), aebfcgdhaebfcgdhaebfcgdhefgh)

    # def test_35(self):
    #     self.assertEqual(fn(word1 = "short", word2 = "longersecondword"), slhoonrgtersecondword)

    # def test_36(self):
    #     self.assertEqual(fn(word1 = "", word2 = "notempty"), notempty)

    # def test_37(self):
    #     self.assertEqual(fn(word1 = "notempty", word2 = ""), notempty)

    # def test_38(self):
    #     self.assertEqual(fn(word1 = "", word2 = "abcdefghijklmnopqrstuvwxyz"), abcdefghijklmnopqrstuvwxyz)

    # def test_39(self):
    #     self.assertEqual(fn(word1 = "aabbccddeeff", word2 = "gggghhhhiiii"), agagbgbgchchdhdheieififi)

    # def test_40(self):
    #     self.assertEqual(fn(word1 = "", word2 = "abcde"), abcde)

    # def test_41(self):
    #     self.assertEqual(fn(word1 = "a1b2c3d4", word2 = "e5f6g7"), ae15bf26cg37d4)

    # def test_42(self):
    #     self.assertEqual(fn(word1 = "oddlength", word2 = "evenlengths"), oedvdelnelnegntghths)

    # def test_43(self):
    #     self.assertEqual(fn(word1 = "same", word2 = "size"), ssaimzee)

    # def test_44(self):
    #     self.assertEqual(fn(word1 = "abcdefg", word2 = "hijklmnopqrstuvwxyz"), ahbicjdkelfmgnopqrstuvwxyz)

    # def test_45(self):
    #     self.assertEqual(fn(word1 = "aabbccddeeffgghhiijj", word2 = "kkllmmnnooppqqrrssttuuvvwwxxyyzz"), akakblblcmcmdndneoeofpfpgqgqhrhrisisjtjtuuvvwwxxyyzz)

    # def test_46(self):
    #     self.assertEqual(fn(word1 = "hello", word2 = "worldwide"), hweolrllodwide)

    # def test_47(self):
    #     self.assertEqual(fn(word1 = "xyzxyzxyz", word2 = "abcabcabc"), xaybzcxaybzcxaybzc)

    # def test_48(self):
    #     self.assertEqual(fn(word1 = "abcdxyz", word2 = "efghwvu"), aebfcgdhxwyvzu)

    # def test_49(self):
    #     self.assertEqual(fn(word1 = "short", word2 = "averylongstring"), sahvoerrtylongstring)

    # def test_50(self):
    #     self.assertEqual(fn(word1 = "a", word2 = "b", word3 = "c"), Error: Solution.mergeAlternately() got an unexpected keyword argument 'word3')

    # def test_51(self):
    #     self.assertEqual(fn(word1 = "hello", word2 = "worldthisisaverylongstring"), hweolrllodthisisaverylongstring)

    # def test_52(self):
    #     self.assertEqual(fn(word1 = "abcdefg", word2 = "hijkl"), ahbicjdkelfg)

    # def test_53(self):
    #     self.assertEqual(fn(word1 = "abcdef", word2 = "ghijklmnop"), agbhcidjekflmnop)

    # def test_54(self):
    #     self.assertEqual(fn(word1 = "abcdabcdabcd", word2 = "xyzxyzxyzxyz"), axbyczdxaybzcxdyazbxcydz)

    # def test_55(self):
    #     self.assertEqual(fn(word1 = "averyveryverylongword", word2 = "short"), asvheorrytveryverylongword)

    # def test_56(self):
    #     self.assertEqual(fn(word1 = "longerword", word2 = "short"), lsohnogretrword)

    # def test_57(self):
    #     self.assertEqual(fn(word1 = "hello", word2 = "world!"), hweolrllod!)

    # def test_58(self):
    #     self.assertEqual(fn(word1 = "nonempty", word2 = ""), nonempty)

    # def test_59(self):
    #     self.assertEqual(fn(word1 = "longstringwithmorecharacters", word2 = "shortstr"), lsohnogrsttsrtirngwithmorecharacters)

    # def test_60(self):
    #     self.assertEqual(fn(word1 = "abcdef", word2 = "zyxwvu"), azbycxdwevfu)

    # def test_61(self):
    #     self.assertEqual(fn(word1 = "onlyone", word2 = ""), onlyone)

    # def test_62(self):
    #     self.assertEqual(fn(word1 = "xyz", word2 = "uvw"), xuyvzw)

    # def test_63(self):
    #     self.assertEqual(fn(word1 = "aabbccddeeff", word2 = "zzzzyyyxxww"), azazbzbzcycydydxexewfwf)

    # def test_64(self):
    #     self.assertEqual(fn(word1 = "abcdefgh", word2 = "ijklmnop"), aibjckdlemfngohp)

    # def test_65(self):
    #     self.assertEqual(fn(word1 = "onetwothree", word2 = "four"), ofnoeutrwothree)

    # def test_66(self):
    #     self.assertEqual(fn(word1 = "aabbcc", word2 = "ddeeff"), adadbebecfcf)

    # def test_67(self):
    #     self.assertEqual(fn(word1 = "aabbccddeeffgghhiijj", word2 = "zzzzzzzzzz"), azazbzbzczczdzdzezezffgghhiijj)

    # def test_68(self):
    #     self.assertEqual(fn(word1 = "abacaxi", word2 = "manga"), ambaancgaaxi)

    # def test_69(self):
    #     self.assertEqual(fn(word1 = "onetwothreefour", word2 = "fivesix"), ofnievtewsoitxhreefour)

    # def test_70(self):
    #     self.assertEqual(fn(word1 = "one", word2 = "twothreefour"), otnweothreefour)

    # def test_71(self):
    #     self.assertEqual(fn(word1 = "merge", word2 = "these", word3 = "strings"), Error: Solution.mergeAlternately() got an unexpected keyword argument 'word3')

    # def test_72(self):
    #     self.assertEqual(fn(word1 = "alphanumeric123", word2 = "characters!@#"), aclhpahraancutmeerrsi!c@1#23)

    # def test_73(self):
    #     self.assertEqual(fn(word1 = "", word2 = "nonempty"), nonempty)

    # def test_74(self):
    #     self.assertEqual(fn(word1 = "xyz", word2 = "wvutsrqponmlkjihgfedcba"), xwyvzutsrqponmlkjihgfedcba)

    # def test_75(self):
    #     self.assertEqual(fn(word1 = "abcde", word2 = ""), abcde)

    # def test_76(self):
    #     self.assertEqual(fn(word1 = "short", word2 = "averyverylongwordindeed"), sahvoerrtyverylongwordindeed)

    # def test_77(self):
    #     self.assertEqual(fn(word1 = "xy", word2 = "abcdefghijk"), xaybcdefghijk)

    # def test_78(self):
    #     self.assertEqual(fn(word1 = "onetwothree", word2 = "fourfivesix"), ofnoeutrwfoitvherseiex)

    # def test_79(self):
    #     self.assertEqual(fn(word1 = "python", word2 = "programming"), ppyrtohgornamming)

    # def test_80(self):
    #     self.assertEqual(fn(word1 = "verylongwordthatgoesonandone", word2 = "short"), vsehroyrltongwordthatgoesonandone)

    # def test_81(self):
    #     self.assertEqual(fn(word1 = "xyz", word2 = "abcdef"), xaybzcdef)

    # def test_82(self):
    #     self.assertEqual(fn(word1 = "merge", word2 = "these"), mtehregsee)

    # def test_83(self):
    #     self.assertEqual(fn(word1 = "abcdefghijklmnopqrstuvwxyz", word2 = "z"), azbcdefghijklmnopqrstuvwxyz)

    # def test_84(self):
    #     self.assertEqual(fn(word1 = "xyzlmnop", word2 = "qrstuvwx"), xqyrzsltmunvowpx)

    # def test_85(self):
    #     self.assertEqual(fn(word1 = "abcdefgh", word2 = "ijklmno"), aibjckdlemfngoh)

    # def test_86(self):
    #     self.assertEqual(fn(word1 = "short", word2 = "averyveryverylongword"), sahvoerrtyveryverylongword)

    # def test_87(self):
    #     self.assertEqual(fn(word1 = "averyverylongwordindeed", word2 = "short"), asvheorrytverylongwordindeed)

    # def test_88(self):
    #     self.assertEqual(fn(word1 = "equal", word2 = "equal"), eeqquuaall)

    # def test_89(self):
    #     self.assertEqual(fn(word1 = "ab", word2 = "cd"), acbd)

    # def test_90(self):
    #     self.assertEqual(fn(word1 = "short", word2 = "averylongstringthatweneedtocheck"), sahvoerrtylongstringthatweneedtocheck)

    # def test_91(self):
    #     self.assertEqual(fn(word1 = "same", word2 = "same"), ssaammee)

    # def test_92(self):
    #     self.assertEqual(fn(word1 = "abcd", word2 = ""), abcd)

    # def test_93(self):
    #     self.assertEqual(fn(word1 = "thisisaverylongstring", word2 = "hello"), thheilsliosaverylongstring)
