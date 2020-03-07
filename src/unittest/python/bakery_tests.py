from lib.Bakery import *
import unittest


class test_bakery(unittest.TestCase):

    def test_empty_input(self):
        bakery = Bakery()
        empty_order = bakery.place_order("")
        self.assertEqual(empty_order, "order empty")

    def test_invalid_code(self):
        bakery = Bakery()
        invalid_code = bakery.place_order("10 Vs5")
        self.assertEqual(invalid_code, "Invalid code")

    def test_invalid_quantity(self):
        bakery = Bakery()
        invalid_quantity = bakery.place_order("10.5 VS5")
        self.assertEqual(invalid_quantity, "Invalid quantity")

    def test_one_code_input(self):
        bakery = Bakery()
        one_code_input = bakery.place_order("10 VS5")
        self.assertEqual(one_code_input, ['17.98'])

    def test_two_code_input(self):
        bakery = Bakery()
        two_code_input = bakery.place_order("10 VS5\n14 MB11")
        self.assertEqual(two_code_input, ['17.98', '47.80'])

    def test_three_code_input(self):
        bakery = Bakery()
        three_code_input = bakery.place_order("10 VS5\n14 MB11\n13 CF")
        self.assertEqual(three_code_input, ['17.98', '47.80', '25.85'])

    def test_redundant_code_input(self):
        bakery = Bakery()
        redundant_code_input = bakery.place_order("10 VS5\n13 CF\n 10 VS5")
        self.assertEqual(redundant_code_input, ['17.98', '25.85', '17.98'])

    def test_three_order_input(self):
        bakery = Bakery()
        one_code_input = bakery.place_order("58 VS5\n49 MB11\n37 CF")
        self.assertEqual(one_code_input, ['105.88', '159.60', '70.87'])


if __name__ == '__main__':
    unittest.main()
