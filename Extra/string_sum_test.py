import unittest
from string_sum import add, parse_numbers

class AddTestCase(unittest.TestCase):

    def test_add_empty(self):
        number = add("")
        self.assertEqual(number, 0)

    def test_add_one(self):
        number = add("1")
        self.assertEqual(number, 1)

    def test_add_two(self):
        number = add("1,2")
        self.assertEqual(number, 3)

    def test_parse_numbers(self):
        list = parse_numbers("1,2")
        self.assertEqual(list, [1, 2])

    def test_parse_numbers_zero(self):
        list = parse_numbers("1,0,2")
        self.assertEqual(list, [1, 0, 2])

    def test_add_lots(self):
        number = add("1,2,3,4,5")
        self.assertEqual(15, number)

    def test_add_newline(self):
        number = add("1\n2\n3")
        self.assertEqual(6, number)

if __name__ == "__main__":
    unittest.main()