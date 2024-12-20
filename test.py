#実行コマンド
#python test.py -v

import unittest
import BakenCombinationCalculator as Calc

#馬連フォーメーションの計算テスト
class TestUmaren(unittest.TestCase):
    def test_umaren_1(self):
        value1 = [1,2]
        value2 = [1,2,3,4]
        excepted = 5
        actual = Calc.calculate_umaren_formation_points(value1, value2)
        self.assertEqual(excepted, actual)

#馬単フォーメーションの計算テスト
class TestUmatan(unittest.TestCase):
    def test_umatan_1(self):
        value1 = [1,2]
        value2 = [1,2,3,4]
        excepted = 6
        actual = Calc.calculate_umatan_formation_points(value1, value2)
        self.assertEqual(excepted, actual)

#3連複フォーメーションの計算テスト
class Test3renpuku(unittest.TestCase):
    def test_3renpuku_1(self):
        value1 = [1,2]
        value2 = [1,2,3,4]
        value3 = [1,2,3,4,5,6,7,8]
        expected = 24
        actual = Calc.calculate_3renpuku_formation_points(value1, value2, value3)
        self.assertEqual(expected, actual)

    def test_3renpuku_2(self):
        value1 = [1,2,3]
        value2 = [4,5,6]
        value3 = [7,8,9,10]
        expected = 36
        actual = Calc.calculate_3renpuku_formation_points(value1, value2, value3)
        self.assertEqual(expected, actual)

    def test_3renpuku_3(self):
        value1 = [1,2,3,4,5,6,7]
        value2 = [1,2,3,4,5,6,7]
        value3 = [1,2,3,4,5,6,7]
        expected = 35
        actual = Calc.calculate_3renpuku_formation_points(value1, value2, value3)
        self.assertEqual(expected, actual)

#3連単フォーメーションの計算テスト
class Test3rentan(unittest.TestCase):
    def test_3rentan_1(self):
        value1 = [1,2,3]
        value2 = [1,2,3,4]
        value3 = [1,2,3,4,5,6,7,8]
        expected = 54
        actual = Calc.calculate_3rentan_formation_points(value1, value2, value3)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()