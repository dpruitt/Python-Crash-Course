import unittest
from employee import Employee


class EmployeeTest(unittest.TestCase):

    def setUp(self):
        self.employee = Employee("Awesome", "Dude", 5000)

    def test_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(10000, self.employee.salary)

    def test_big_raise(self):
        self.employee.give_raise(50000)
        self.assertEqual(55000, self.employee.salary)
