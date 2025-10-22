# -*- coding: utf-8 -*-

"""
TDD Manifesto unit testing examples
"""

import unittest
from TDD_Manifesto.TDD_Manifesto_exercises import(
    fizz_buzz,
)


class TestFizzBuzz(unittest.TestCase):
    """
    FizzBuzz unittest class.
    """

    def test_GivenANumberAsInput_whenFizzBuzzFunctionGetsTheInput_thenTheNumberIsPrintAsSring(self):
        
        number_as_input = 0

        test_string_output = fizz_buzz(number_as_input)

        self.assertEqual(test_string_output,"0")

    def test_GivenACharacterAsInput_whenFizzBuzzFunctionGetsTheInput_thenTheFunctionFails(self):

        character_as_input = "a"

        self.assertRaises(ValueError, fizz_buzz, character_as_input)

    def test_GivenAMultipleOfThreeAsInput_whenFizzBuzzFunctionGetsTheInput_thenTheFunctionPrintsFizz(self):

        number_as_input = 3

        test_string_output = fizz_buzz(number_as_input)        

        self.assertEqual(test_string_output, "Fizz")

    def test_GivenAMultipleOfFiveAsInput_whenFizzBuzzFunctionGetsTheInput_thenTheFunctionPrintsBuzz(self):

        number_as_input = 5

        test_string_output = fizz_buzz(number_as_input)        

        self.assertEqual(test_string_output, "Buzz")

    def test_GivenAMultipleOfThreeAndFiveAsInput_whenFizzBuzzFunctionGetsTheInput_thenTheFunctionPrintsFizzBuzz(self):

        number_as_input = 15

        test_string_output = fizz_buzz(number_as_input)        

        self.assertEqual(test_string_output, "FizzBuzz")
