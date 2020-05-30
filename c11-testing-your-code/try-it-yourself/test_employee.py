import unittest

from employee import Employee

class EmployeeTestCase(unittest.TestCase):

    def setUp(self):
        """ first = "cesar"
        last = 'rodriguez'
        annual_salary = 10000 """
        self.employee = Employee('cesar', 'rodriguez', 10000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEquals(self.employee.annual_salary, 15000)
    
    def test_give_custom_raise(self):
        self.employee.give_raise(10000)
        self.assertEquals(self.employee.annual_salary, 20000)

    

if __name__ == "__main__":
    unittest.main()