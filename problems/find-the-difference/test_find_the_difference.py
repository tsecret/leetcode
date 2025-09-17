import unittest
from solution_find_the_difference import Solution

fn = Solution().findTheDifference

class Test(unittest.TestCase):

    def test_0(self):
        self.assertEqual(fn(s = "abcd", t = "abcde"), "e")

    def test_1(self):
        self.assertEqual(fn(s = "aeiou", t = "aeiouf"), "f")

    def test_2(self):
        self.assertEqual(fn(s = "python", t = "ypthon"), None)

    def test_3(self):
        self.assertEqual(fn(s = "abcdxyz", t = "abcdzyxw"), "w")

    def test_4(self):
        self.assertEqual(fn(s = "a", t = "ab"), "b")

    def test_5(self):
        self.assertEqual(fn(s = "xyz", t = "zyxw"), "w")

    def test_6(self):
        self.assertEqual(fn(s = "", t = "y"), "y")

    def test_7(self):
        self.assertEqual(fn(s = "abcdefghijklmnopqrstuvwxyz", t = "abcdefghijklmnopqrstuvwxyza"), "a")

    def test_8(self):
        self.assertEqual(fn(s = "hello", t = "helloa"), "a")

    def test_9(self):
        self.assertEqual(fn(s = "hello", t = "hleloa"), "a")

    def test_10(self):
        self.assertEqual(fn(s = "aeiou", t = "aeiozu"), "z")

    def test_11(self):
        self.assertEqual(fn(s = "hello", t = "ohell"), None)

    def test_12(self):
        self.assertEqual(fn(s = "ae", t = "aea"), "a")

    def test_13(self):
        self.assertEqual(fn(s = "abcdefghijklmnopqrstuvwxyz", t = "abcdefghijklmnopqrstuvwxyzp"), "p")

    def test_14(self):
        self.assertEqual(fn(s = "thisisaverylongstringfortesting", t = "thisisaverylongstringfortestingz"), "z")

    def test_15(self):
        self.assertEqual(fn(s = "thisisaverylongstringwithalotofcharacters", t = "thisisaverylongstringwithalotofcharactersz"), "z")

    def test_16(self):
        self.assertEqual(fn(s = "almostsame", t = "almostsamee"), "e")

    def test_17(self):
        self.assertEqual(fn(s = "abcdabcdabcdabcdabcdabcd", t = "abcdabcdabcdabcdabcdabcde"), "e")

    def test_18(self):
        self.assertEqual(fn(s = "thisisaverylongstringwithsomerepeatingcharacters", t = "thisisaverylongstringwithsomerepeatingcharactersist"), "i")

    def test_19(self):
        self.assertEqual(fn(s = "sameletters", t = "samesletters"), "s")

    def test_20(self):
        self.assertEqual(fn(s = "mississippi", t = "mississippix"), "x")

    def test_21(self):
        self.assertEqual(fn(s = "thisisaverylongstringthatcontainsavarietyofcharacters", t = "thisisaverylongstringthatcontainsavarietyofcharactorst"), "o")

    def test_22(self):
        self.assertEqual(fn(s = "mississippi", t = "mississippiw"), "w")

    def test_23(self):
        self.assertEqual(fn(s = "samechar", t = "samechars"), "s")

    def test_24(self):
        self.assertEqual(fn(s = "quickbrownfoxjumps", t = "quickbrownfoxjumpsl"), "l")

    def test_25(self):
        self.assertEqual(fn(s = "pythonprogramming", t = "pythonprogrammingz"), "z")

    def test_26(self):
        self.assertEqual(fn(s = "singlecharacter", t = "singlecharacterr"), "r")

    def test_27(self):
        self.assertEqual(fn(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz", t = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzj"), "j")

    def test_28(self):
        self.assertEqual(fn(s = "abcdabcdabcd", t = "abcdabcdabcdd"), "d")

    def test_29(self):
        self.assertEqual(fn(s = "uniqueletters", t = "uniquelettersx"), "x")

    def test_30(self):
        self.assertEqual(fn(s = "xyzzzxyzzz", t = "xyzzzxyzzzx"), "x")

    def test_31(self):
        self.assertEqual(fn(s = "alibabacloud", t = "alibabacloudu"), "u")

    def test_32(self):
        self.assertEqual(fn(s = "xyxzyzy", t = "xyxzyzyz"), "z")

    def test_33(self):
        self.assertEqual(fn(s = "abcdabcdabcd", t = "abcdabcdabcdx"), "x")

    def test_34(self):
        self.assertEqual(fn(s = "different", t = "differenti"), "i")

    def test_35(self):
        self.assertEqual(fn(s = "finding", t = "findinwg"), "w")

    def test_36(self):
        self.assertEqual(fn(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz", t = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"), "z")

    def test_37(self):
        self.assertEqual(fn(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz", t = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzx"), "x")

    def test_38(self):
        self.assertEqual(fn(s = "onemore", t = "onemroem"), "m")

    def test_39(self):
        self.assertEqual(fn(s = "hellothereeveryone", t = "hellothereeveryonex"), "x")

    def test_40(self):
        self.assertEqual(fn(s = "mississippi", t = "mississippip"), "p")

    def test_41(self):
        self.assertEqual(fn(s = "pneumonoultramicroscopicsilicovolcanoconiosis", t = "pneumonoultramicroscopicsilicovolcanoconiosisp"), "p")

    def test_42(self):
        self.assertEqual(fn(s = "quickbrownfoxjumpsoverthelazydog", t = "quickbrownfoxjumpsoverthelazydogg"), "g")

    def test_43(self):
        self.assertEqual(fn(s = "hellothisisanexample", t = "thisisanexamplehelloo"), "o")

    def test_44(self):
        self.assertEqual(fn(s = "short", t = "horst"), None)

    def test_45(self):
        self.assertEqual(fn(s = "abracadabra", t = "abracadabrak"), "k")

    def test_46(self):
        self.assertEqual(fn(s = "pythonprogramming", t = "pythonprogrammings"), "s")

    def test_47(self):
        self.assertEqual(fn(s = "mamamamamamama", t = "mmamamamamamama"), "m")

    def test_48(self):
        self.assertEqual(fn(s = "qwert", t = "wqret"), None)

    def test_49(self):
        self.assertEqual(fn(s = "repeatedcharactershhhhh", t = "repeatedcharactershhhhha"), "a")

    def test_50(self):
        self.assertEqual(fn(s = "abcdabcdabcd", t = "abcdabcdabcde"), "e")

    def test_51(self):
        self.assertEqual(fn(s = "abcdabcd", t = "abcdabcde"), "e")

    def test_52(self):
        self.assertEqual(fn(s = "uniqueletters", t = "enuiqtelrstsu"), "s")

    def test_53(self):
        self.assertEqual(fn(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzaaa", t = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzaaab"), "b")

    def test_54(self):
        self.assertEqual(fn(s = "uniquecharacters", t = "uniquecharactersn"), "n")

    def test_55(self):
        self.assertEqual(fn(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz", t = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"), "z")

    def test_56(self):
        self.assertEqual(fn(s = "qwertypoiuytrewq", t = "qwertypoiuytrewqa"), "a")

    def test_57(self):
        self.assertEqual(fn(s = "abcdefghijklnmopqrstuvwxyz", t = "zyxwvutsrqponmlkjihgfedcbaq"), "q")

    def test_58(self):
        self.assertEqual(fn(s = "samecharacters", t = "samecharactersc"), "c")

    def test_59(self):
        self.assertEqual(fn(s = "specialcharacters!@#$%^&*()", t = "specialcharacters!@#$%^&*()s"), "s")

    def test_60(self):
        self.assertEqual(fn(s = "repeatedletters", t = "repeadetletters"), None)

    def test_61(self):
        self.assertEqual(fn(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz", t = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzz"), "z")

    def test_62(self):
        self.assertEqual(fn(s = "abcdefghijklmnopqrstuvwxyz", t = "abcdefghijklmnopqrstuvwxyzq"), "q")

    def test_63(self):
        self.assertEqual(fn(s = "onetwothree", t = "onetwothreefour"), "f")

    def test_64(self):
        self.assertEqual(fn(s = "short", t = "shorrt"), "r")

    def test_65(self):
        self.assertEqual(fn(s = "uniqueletters", t = "eniqulettersu"), None)

    def test_66(self):
        self.assertEqual(fn(s = "quickbrownfoxjumpsoverthelazydog", t = "quickbrownfoxjumpsoverthelazydogq"), "q")

    def test_67(self):
        self.assertEqual(fn(s = "onetwothree", t = "onetwothreef"), "f")

    def test_68(self):
        self.assertEqual(fn(s = "hellothere", t = "hellotherex"), "x")

    def test_69(self):
        self.assertEqual(fn(s = "uniqueletter", t = "uniqueletteru"), "u")

    def test_70(self):
        self.assertEqual(fn(s = "uniqueletters", t = "enuiqueletters"), "e")

    def test_71(self):
        self.assertEqual(fn(s = "thisisalongstring", t = "thisisalongstringx"), "x")

    def test_72(self):
        self.assertEqual(fn(s = "nogapsbetweenletters", t = "nogapsbetweenlettersn"), "n")

    def test_73(self):
        self.assertEqual(fn(s = "abcdefg", t = "gfedcbaa"), "a")

    def test_74(self):
        self.assertEqual(fn(s = "repeated", t = "repeatedr"), "r")

    def test_75(self):
        self.assertEqual(fn(s = "pythonprogramming", t = "pythonprogrammingg"), "g")

    def test_76(self):
        self.assertEqual(fn(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz", t = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzb"), "b")

    def test_77(self):
        self.assertEqual(fn(s = "balloon", t = "ooblaanl"), "a")

    def test_78(self):
        self.assertEqual(fn(s = "sameletters", t = "smaleetters"), None)

    def test_79(self):
        self.assertEqual(fn(s = "randomstring", t = "randomstrings"), "s")

    def test_80(self):
        self.assertEqual(fn(s = "uniqueletters", t = "uniqueletterst"), "t")

    def test_81(self):
        self.assertEqual(fn(s = "thequickbrownfoxjumpsoverthelazydog", t = "thequickbrownfoxjumpsoverthelazydoga"), "a")

    def test_82(self):
        self.assertEqual(fn(s = "xyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxz", t = "xyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzyxzj"), "j")

    def test_83(self):
        self.assertEqual(fn(s = "quickbrownfoxjumpsoverthelazydog", t = "quickbrownfoxjumpsoverthelazydogm"), "m")

    def test_84(self):
        self.assertEqual(fn(s = "thequickbrownfoxjumpsoverthelazydog", t = "thequickbrownfoxjumpsoverthelazydogp"), "p")

    def test_85(self):
        self.assertEqual(fn(s = "xyzz", t = "xyzzz"), "z")

    def test_86(self):
        self.assertEqual(fn(s = "repeatedlettersinthisstring", t = "repeatedlettersinthisstringi"), "i")

    def test_87(self):
        self.assertEqual(fn(s = "aaaabbbbccccddddeee", t = "aaaabbbbccccddddeeef"), "f")

    def test_88(self):
        self.assertEqual(fn(s = "zzzzzzzzzz", t = "zzzzzzzzzzz"), "z")

    def test_89(self):
        self.assertEqual(fn(s = "abcdefghijklmnopqrstuvwxyz", t = "abcdefghijklmnopqrstuvwxyzz"), "z")

    def test_90(self):
        self.assertEqual(fn(s = "thesameletterrepeatedseveraltime", t = "thesameletterrepeatedseveraltimee"), "e")

    def test_91(self):
        self.assertEqual(fn(s = "duplicatecharacters", t = "duplicatecharacterst"), "t")

    def test_92(self):
        self.assertEqual(fn(s = "complexinputwithdifferentcharacters", t = "complexinputwithdifferentcharactersg"), "g")

    def test_93(self):
        self.assertEqual(fn(s = "abcdefghijklmnopqrstuvwxyz", t = "abcdefghijklmnopqrstuvwxyzx"), "x")

    def test_94(self):
        self.assertEqual(fn(s = "pythonprogramming", t = "pythonprogrammingo"), "o")

    def test_95(self):
        self.assertEqual(fn(s = "xyzz", t = "xyzzy"), "y")
