import unittest
from rectangle import area
from rectangle import perimeter


class RectangleAreaTestCase(unittest.TestCase):
    def test_area_1(self):
        res = area(56743, 1)
        self.assertEqual(res, 56743)

    def test_area_2(self):
        res = area(0, 157)
        self.assertEqual(res, 0)

    def test_area_3(self):
        res = area(5647, 0)
        self.assertEqual(res, 0)

    def test_big_area_1(self):
        res = area(1000000000000000000, 20)
        self.assertEqual(res, 20000000000000000000)

    def test_big_area_2(self):
        res = area(1234567890, 9876543210)
        self.assertEqual(res, 1234567890 * 9876543210)

    def test_big_area_3(self):
        res = area(1000000000000000000, 1000000000000000000)
        self.assertEqual(res, 1000000000000000000000000000000000000)

    def test_wrong_value_area_1(self):
        with self.assertRaises(ValueError):
            area(-124, 3)

    def test_wrong_value_area_2(self):
        with self.assertRaises(ValueError):
            area(-4.2, 1)

    def test_wrong_value_area_3(self):
        with self.assertRaises(ValueError):
            area(-10000000000000000000000000000, 65)

    def test_wrong_type_area_1(self):
        with self.assertRaises(TypeError):
            area("okr", "sdvg")

    def test_wrong_type_area_2(self):
        with self.assertRaises(TypeError):
            area([541, 124], [8765544, 7654])

    def test_wrong_type_area_3(self):
        with self.assertRaises(TypeError):
            area(True, False)


class RectanglePerimetrTestCase(unittest.TestCase):
    def test_perimetr_1(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_perimetr_2(self):
        res = perimeter(1, 341)
        self.assertEqual(res, 684)

    def test_perimetr_3(self):
        res = perimeter(15, 34)
        self.assertEqual(res, 98)

    def test_big_perimetr_1(self):
        res = perimeter(1000000000000000000, 1)
        self.assertEqual(res, 2000000000000000002)

    def test_big_perimetr_2(self):
        res = perimeter(1234567890, 9876543210)
        self.assertEqual(res, (1234567890 + 9876543210) * 2)

    def test_big_perimetr_3(self):
        res = perimeter(1000000000000000000, 1000000000000000000)
        self.assertEqual(res, 4000000000000000000)

    def test_wrong_value_perimetr_1(self):
        with self.assertRaises(ValueError):
            perimeter(-124, 3)

    def test_wrong_value_perimetr_2(self):
        with self.assertRaises(ValueError):
            perimeter(-4.2, 1)

    def test_wrong_value_perimetr_3(self):
        with self.assertRaises(ValueError):
            perimeter(-10000000000000000000000000000, 65)

    def test_wrong_type_perimetr_1(self):
        with self.assertRaises(TypeError):
            perimeter("okr", "sdvg")

    def test_wrong_type_perimetr_2(self):
        with self.assertRaises(TypeError):
            perimeter([541, 124], [8765544, 7654])

    def test_wrong_type_perimetr_3(self):
        with self.assertRaises(TypeError):
            perimeter(True, False)