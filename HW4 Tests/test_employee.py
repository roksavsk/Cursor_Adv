from employee import Employee
import unittest
from unittest.mock import patch


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.classTest = Employee("Jake", "McKenzie", 1000)

    def test_email(self):
        self.assertEqual(self.classTest.email, "Jake.McKenzie@email.com")

    def test_fullname(self):
        self.assertEqual(self.classTest.fullname, "Jake McKenzie")

    def test_apply_raise(self):
        self.classTest.apply_raise()
        self.assertEqual(self.classTest.pay, 1050)

    @patch("employee.requests.get")
    def test_monthly_schedule(self, mock_get):
        mock_get.return_value.ok = True
        mock_get.return_value.text = "All ok"
        response = self.classTest.monthly_schedule("May")
        print(response)
        self.assertEqual(response, "All ok")
        mock_get.return_value.ok = False
        response = self.classTest.monthly_schedule("May")
        print(response)
        self.assertEqual(response, "Bad Response!")


if __name__ == '__main__':
    unittest.main()
