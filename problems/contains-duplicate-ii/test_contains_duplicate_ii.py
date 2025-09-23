import unittest
from solution_contains_duplicate_ii import Solution

fn = Solution().containsNearbyDuplicate

class Test(unittest.TestCase):

    def test_0(self):
        self.assertEqual(fn(nums = [1000000000,-1000000000,1000000000,-1000000000], k = 2), True)

    def test_1(self):
        self.assertEqual(fn(nums = [1,2,3,4,5,6,7,8,9,10], k = 8), False)

    def test_2(self):
        self.assertEqual(fn(nums = [1,0,1,1], k = 1), True)

    def test_3(self):
        self.assertEqual(fn(nums = [0,1,2,3,4,5,6,7,8,9,0], k = 10), True)

    def test_4(self):
        self.assertEqual(fn(nums = [1,2,3,4,5,6,7,8,9,9], k = 1), True)

    def test_5(self):
        self.assertEqual(fn(nums = [1,2,2,1], k = 2), True)

    def test_6(self):
        self.assertEqual(fn(nums = [1,2,3,4,5], k = 4), False)

    def test_7(self):
        self.assertEqual(fn(nums = [1,2,3,4,5], k = 5), False)

    def test_8(self):
        self.assertEqual(fn(nums = [1,2,3,4,5,6,7,8,9,10], k = 5), False)

    def test_9(self):
        self.assertEqual(fn(nums = [1,2,3,4,5,6,7,8,9,1], k = 9), True)

    def test_10(self):
        self.assertEqual(fn(nums = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1], k = 18), True)

    def test_11(self):
        self.assertEqual(fn(nums = [9,9], k = 1), True)

    def test_12(self):
        self.assertEqual(fn(nums = [9,1,2,3,9], k = 4), True)

    def test_13(self):
        self.assertEqual(fn(nums = [1], k = 0), False)

    def test_14(self):
        self.assertEqual(fn(nums = [1,2,3,1], k = 3), True)

    def test_15(self):
        self.assertEqual(fn(nums = [999999999,999999999,1,1], k = 2), True)

    def test_16(self):
        self.assertEqual(fn(nums = [999999999,-999999999,999999999], k = 2), True)

    def test_17(self):
        self.assertEqual(fn(nums = [1,2,2], k = 2), True)

    def test_18(self):
        self.assertEqual(fn(nums = [1,2,3,4,5,6,7,8,9,1], k = 8), False)

    def test_19(self):
        self.assertEqual(fn(nums = [1,1], k = 0), False)

    def test_20(self):
        self.assertEqual(fn(nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,1], k = 20), True)

    def test_21(self):
        self.assertEqual(fn(nums = [1,2,3,1,2,3], k = 2), False)

    def test_22(self):
        self.assertEqual(fn(nums = [1,2,3,4,5,6,7,8,9,10], k = 0), False)

    def test_23(self):
        self.assertEqual(fn(nums = [1,1,1,1,1,1,1,1,1,1], k = 1), True)

    def test_24(self):
        self.assertEqual(fn(nums = [0,0,0,0,0,0,0,0,0,0], k = 3), True)

    def test_25(self):
        self.assertEqual(fn(nums = [1,2,1,2,1,2,1,2], k = 1), False)

    def test_26(self):
        self.assertEqual(fn(nums = [1,2,3,4,5,6,7,8,9,1], k = 7), False)

    def test_27(self):
        self.assertEqual(fn(nums = [1,0,2,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0], k = 1), False)

    def test_28(self):
        self.assertEqual(fn(nums = [999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991, 999999999], k = 9), True)

    def test_29(self):
        self.assertEqual(fn(nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,1], k = 1), False)

    def test_30(self):
        self.assertEqual(fn(nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], k = 1), True)

    def test_31(self):
        self.assertEqual(fn(nums = [10,20,30,40,50,60,70,80,90,100,10], k = 10), True)

    def test_32(self):
        self.assertEqual(fn(nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,50], k = 49), True)

    def test_33(self):
        self.assertEqual(fn(nums = [5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1], k = 2), True)

    def test_34(self):
        self.assertEqual(fn(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 1, 1], k = 20), True)

    def test_35(self):
        self.assertEqual(fn(nums = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10], k = 10), True)

    def test_36(self):
        self.assertEqual(fn(nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,1,2,3,4,5], k = 49), False)

    def test_37(self):
        self.assertEqual(fn(nums = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1], k = 10), True)

    def test_38(self):
        self.assertEqual(fn(nums = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], k = 20), True)

    def test_39(self):
        self.assertEqual(fn(nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,1], k = 10), False)

    def test_40(self):
        self.assertEqual(fn(nums = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1], k = 9), True)

    def test_41(self):
        self.assertEqual(fn(nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,1], k = 20), True)

    def test_42(self):
        self.assertEqual(fn(nums = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10], k = 1), False)

    def test_43(self):
        self.assertEqual(fn(nums = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1], k = 10), True)

    def test_44(self):
        self.assertEqual(fn(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], k = 1), True)

    def test_45(self):
        self.assertEqual(fn(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 1, 1], k = 1), True)

    def test_46(self):
        self.assertEqual(fn(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1], k = 10), True)

    def test_47(self):
        self.assertEqual(fn(nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,30], k = 29), True)

    def test_48(self):
        self.assertEqual(fn(nums = [1000000000, 1000000000, 1, 2, 3], k = 1), True)

    def test_49(self):
        self.assertEqual(fn(nums = [1000000000,-1000000000,1000000000,-1000000000,1000000000], k = 2), True)

    def test_50(self):
        self.assertEqual(fn(nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], k = 20), True)

    def test_51(self):
        self.assertEqual(fn(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1], k = 14), False)

    def test_52(self):
        self.assertEqual(fn(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9], k = 9), True)

    def test_53(self):
        self.assertEqual(fn(nums = [0,0,1,1,2,2,3,3,4,4], k = 1), True)

    def test_54(self):
        self.assertEqual(fn(nums = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9], k = 8), False)

    def test_55(self):
        self.assertEqual(fn(nums = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9], k = 17), True)

    def test_56(self):
        self.assertEqual(fn(nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,1], k = 0), False)

    def test_57(self):
        self.assertEqual(fn(nums = [1000000000, 999999999, 1000000000, 999999999, 1000000000, 999999999], k = 2), True)

    def test_58(self):
        self.assertEqual(fn(nums = [1000000000, 1000000000], k = 1), True)

    def test_59(self):
        self.assertEqual(fn(nums = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10], k = 5), False)

    def test_60(self):
        self.assertEqual(fn(nums = [1,2,3,4,5,1,2,3,4,5], k = 4), False)

    def test_61(self):
        self.assertEqual(fn(nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,1], k = 29), False)

    def test_62(self):
        self.assertEqual(fn(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 10), False)

    def test_63(self):
        self.assertEqual(fn(nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], k = 20), False)

    def test_64(self):
        self.assertEqual(fn(nums = [10,20,30,40,50,60,70,80,90,10], k = 9), True)

    def test_65(self):
        self.assertEqual(fn(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1], k = 9), True)

    def test_66(self):
        self.assertEqual(fn(nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,1], k = 49), False)

    def test_67(self):
        self.assertEqual(fn(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], k = 5), True)

    def test_68(self):
        self.assertEqual(fn(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1], k = 10), True)

    def test_69(self):
        self.assertEqual(fn(nums = [-1000000000, -2000000000, -1000000000, -3000000000, -2000000000], k = 2), True)

    def test_70(self):
        self.assertEqual(fn(nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,1], k = 100000), True)

    def test_71(self):
        self.assertEqual(fn(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1], k = 18), True)

    def test_72(self):
        self.assertEqual(fn(nums = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1], k = 8), False)

    def test_73(self):
        self.assertEqual(fn(nums = [1000000000, 1000000001, 1000000002, 1000000003, 1000000004, 1000000005, 1000000006, 1000000007, 1000000008, 1000000009, 1000000000], k = 10), True)

    def test_74(self):
        self.assertEqual(fn(nums = [10,1,2,10,3,4,5,10,6,7,8,9,10], k = 8), True)

    def test_75(self):
        self.assertEqual(fn(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], k = 1), True)

    def test_76(self):
        self.assertEqual(fn(nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,1], k = 24), False)

    def test_77(self):
        self.assertEqual(fn(nums = [1,0,1,1,0,1,0,1], k = 2), True)

    def test_78(self):
        self.assertEqual(fn(nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,1], k = 19), False)

    def test_79(self):
        self.assertEqual(fn(nums = [1,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,20], k = 20), True)

    def test_80(self):
        self.assertEqual(fn(nums = [1,0,1,1,0,1,0,1,0,1,0,1], k = 1), True)

    def test_81(self):
        self.assertEqual(fn(nums = [5,5,5,5,5,5,5,5,5,5], k = 5), True)

    def test_82(self):
        self.assertEqual(fn(nums = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1], k = 5), False)

    def test_83(self):
        self.assertEqual(fn(nums = [1000000000, 2000000000, 1000000000, 3000000000, 2000000000], k = 2), True)

    def test_84(self):
        self.assertEqual(fn(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1], k = 20), True)

    def test_85(self):
        self.assertEqual(fn(nums = [1000000000, 2000000000, 1000000000], k = 2), True)

    def test_86(self):
        self.assertEqual(fn(nums = [1,2,3,4,5,6,7,8,9,10,1], k = 10), True)

    def test_87(self):
        self.assertEqual(fn(nums = [1,0,1,1,0,1,0,1,0,1], k = 2), True)

    def test_88(self):
        self.assertEqual(fn(nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], k = 19), False)

    def test_89(self):
        self.assertEqual(fn(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9], k = 10), True)

    def test_90(self):
        self.assertEqual(fn(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0], k = 10), True)

    def test_91(self):
        self.assertEqual(fn(nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,1], k = 30), True)

    def test_92(self):
        self.assertEqual(fn(nums = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,1,2,3,4,5,6,7,8,9,10], k = 5), False)

    def test_93(self):
        self.assertEqual(fn(nums = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,1,2,3,4,5], k = 10), False)

    def test_94(self):
        self.assertEqual(fn(nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,1], k = 39), False)

    def test_95(self):
        self.assertEqual(fn(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], k = 1), True)

    def test_96(self):
        self.assertEqual(fn(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 1], k = 2), True)

    def test_97(self):
        self.assertEqual(fn(nums = [1000000000, -1000000000, 1000000000, -1000000000], k = 2), True)

    def test_98(self):
        self.assertEqual(fn(nums = [1,0,1,1,0,1], k = 2), True)

    def test_99(self):
        self.assertEqual(fn(nums = [5, 4, 3, 2, 1, 0, 5, 4, 3, 2, 1, 0], k = 5), False)

    def test_100(self):
        self.assertEqual(fn(nums = [1000000000, 1000000001, 1000000000, 1000000001, 1000000000], k = 2), True)

    def test_101(self):
        self.assertEqual(fn(nums = [1,1,2,2,3,3,4,4,5,5], k = 1), True)

    def test_102(self):
        self.assertEqual(fn(nums = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50], k = 4), False)

    def test_103(self):
        self.assertEqual(fn(nums = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19,20,20,1], k = 20), True)

    def test_104(self):
        self.assertEqual(fn(nums = [999999999,999999998,999999997,999999996,999999995,999999994,999999993,999999992,999999991,999999990,999999999], k = 9), False)

    def test_105(self):
        self.assertEqual(fn(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5], k = 10), True)
