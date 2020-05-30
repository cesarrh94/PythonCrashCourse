# HOW TO TEST a WHOLE CLASS

import unittest

from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    
    # the setUp() method: allows you to create these objects once and then use them in each of your 
    # test methods. Python runs the setUp() method before running each method starting with test_.
    def setUp(self):
        """ create a survey and set of responses for use in all test methods. """
        question = "What language do you speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['Spanish', 'English', 'Japanese']

    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn('Spanish', self.my_survey.responses)

    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == "__main__":
    unittest.main()