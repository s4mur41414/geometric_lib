import unittest
from square import area
from square import perimeter


class SquareAreaTestCase(unittest.TestCase):
    def test_area_1(self):
        res = area(13)
        self.assertEqual(res, 169)

    def test_area_2(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_3(self):
        res = area(45)
        self.assertEqual(res, 2025)

    def test_big_area_1(self):
        res = area(1000000000000000000)
        self.assertEqual(res, 1000000000000000000000000000000000000)

    def test_big_area_2(self):
        res = area(1234567890)
        self.assertEqual(res, 1234567890 * 1234567890)

    def test_big_area_3(self):
        res = area(987543210)
        self.assertEqual(res, 987543210 * 987543210)

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


class SquarePerimetrTestCase(unittest.TestCase):

    def test_perimetr_1(self):
        res = perimeter(1)
        self.assertEqual(res, 4)

    def test_perimetr_2(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimetr_3(self):
        res = perimeter(100)
        self.assertEqual(res, 400)

    def test_big_perimetr_1(self):
        res = perimeter(1000000000000000000)
        self.assertEqual(res, 4000000000000000000)

    def test_big_perimetr_2(self):
        res = perimeter(1234567890)
        self.assertEqual(res, 4938271560)

    def test_big_perimetr_3(self):
        res = perimeter(9876543210)
        self.assertEqual(res, 9876543210 * 4)

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