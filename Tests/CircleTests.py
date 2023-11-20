import unittest
import math
from circle import area
from circle import perimeter


class CircleAreaTestCase(unittest.TestCase):
    def test_area_1(self):
        res = area(0)
        ans = math.pi * 0
        res = f'{res:.2f}'
        ans = f'{ans:.2f}'
        self.assertEqual(res, ans)

    def test_area_2(self):
        res = area(100)
        ans = math.pi * 10000
        res = f'{res:.2f}'
        ans = f'{ans:.2f}'
        self.assertEqual(res, ans)

    def test_area_3(self):
        res = area(45)
        ans = math.pi * 2025
        res = f'{res:.2f}'
        ans = f'{ans:.2f}'
        self.assertEqual(res, ans)

    def test_big_area_1(self):
        res = area(100000000000000000000)
        ans = math.pi * 10000000000000000000000000000000000000000
        res = f'{res:.2f}'
        ans = f'{ans:.2f}'
        self.assertEqual(res, ans)

    def test_big_area_2(self):
        res = area(1000000000000000000)
        ans = math.pi * 1000000000000000000000000000000000000
        res = f'{res:.2f}'
        ans = f'{ans:.2f}'
        self.assertEqual(res, ans)

    def test_big_area_3(self):
        res = area(1234567890)
        ans = math.pi * 1234567890 * 1234567890
        res = f'{res:.2f}'
        ans = f'{ans:.2f}'
        self.assertEqual(res, ans)

    def test_wrong_value_area_1(self):
        with self.assertRaises(ValueError):
            area(-124)

    def test_wrong_value_area_2(self):
        with self.assertRaises(ValueError):
            area(-4.2)

    def test_wrong_value_area_3(self):
        with self.assertRaises(ValueError):
            area(-10000000000000000000000000000)

    def test_wrong_type_area_1(self):
        with self.assertRaises(TypeError):
            area("okr")

    def test_wrong_type_area_2(self):
        with self.assertRaises(TypeError):
            area([541, 124])

    def test_wrong_type_area_3(self):
        with self.assertRaises(TypeError):
            area(True)


class CirclePerimetrTestCase(unittest.TestCase):
    def test_perimetr_1(self):
        res = perimeter(15)
        self.assertEqual(res, math.pi * 30)

    def test_perimetr_2(self):
        res = perimeter(100)
        self.assertEqual(res, math.pi * 200)

    def test_perimetr_3(self):
        res = perimeter(0)
        self.assertEqual(res, math.pi * 0)

    def test_big_perimetr_1(self):
        res = perimeter(200000000000000000001)
        self.assertEqual(res, math.pi * 400000000000000000002)

    def test_big_perimetr_2(self):
        res = perimeter(1234567890)
        self.assertEqual(res, math.pi * 1234567890 * 2)

    def test_big_perimetr_3(self):
        res = perimeter(1000000000000000000000)
        self.assertEqual(res, math.pi * 2000000000000000000000)

    def test_wrong_value_perimetr_1(self):
        with self.assertRaises(ValueError):
            perimeter(-124)

    def test_wrong_value_perimetr_2(self):
        with self.assertRaises(ValueError):
            perimeter(-4.2)

    def test_wrong_value_perimetr_3(self):
        with self.assertRaises(ValueError):
            perimeter(-10000000000000000000000000000)

    def test_wrong_type_perimetr_1(self):
        with self.assertRaises(TypeError):
            perimeter("sdvg")

    def test_wrong_type_perimetr_2(self):
        with self.assertRaises(TypeError):
            perimeter([123, 423, 124])

    def test_wrong_type_perimetr_3(self):
        with self.assertRaises(TypeError):
            perimeter(False)
