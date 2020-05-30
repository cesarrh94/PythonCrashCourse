""" 
Unit Test: verifies that one specific aspect of a function's behavior is correct.

Test Case: is a collection of unit tests that together prove that a function behaves as it's 
supposed to, within the full range of situations you expect it to handle. A good test case considers
all the possible kinds of input a function could receive and includes test to represent each of these
situations.

A test case with a Full Coverage: includes a full range of unit tests covering all the possible ways
you can use a function. """

# the module unittest is a standard library provides tools for testing your code
import unittest 

from name_function import get_formatted_name

# step 1: create a class to contain the unit test, remember the class must inherit from 
# unittest.TestCase so Python knows how to run the test you write.
class NamesTestCase(unittest.TestCase):
    """ Tests for name_function.py """

    def test_first_last_name(self):
        # step 2: access the function that you will going to test from the module
        formatted_name = get_formatted_name("cesar", "rodriguez")
        # step 3: assert() method, verify that the result you received matches the result you expect to 
        # receive
        self.assertEqual(formatted_name, 'Cesar Rodriguez')

# step 4 
if __name__ == "__main__":
    unittest.main()