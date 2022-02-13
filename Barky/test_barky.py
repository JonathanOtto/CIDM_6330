import unittest
import os
import barky
import commands

class BarkyTestCase(unittest.TestCase):
    def test_working(self):
        pass

    def test_option_choice_is_valid(self):

        #arrange
        option_q = barky.Option("A", ["A","B","T","E","D","G","Q"])
        expected_value = True
        #act
        actual_value = option_q.option_choice_is_valid
        #assert
        self.assertEqual(expected_value, actual_value)