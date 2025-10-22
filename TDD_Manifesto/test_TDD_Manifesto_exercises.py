# -*- coding: utf-8 -*-

"""
TDD Manifesto unit testing examples
"""

import unittest
from TDD_Manifesto.TDD_Manifesto_exercises import(
    add_number,
    fizz_buzz,
)


class TestFizzBuzz(unittest.TestCase):
    """
    FizzBuzz unittest class.
    """

    def test_GivenANumberAsInput_whenFizzBuzzFunctionGetsTheInput_thenTheNumberIsPrintAsSring(self):
        
        number_as_input = 0

        test_string_output = fizz_buzz(number_as_input)

        self.assertEqual(test_string_output, "0")
    
    def test_GivenANegativeNumberAsInput_whenFizzBuzzFunctionGetsTheInput_thenTheNumberIsPrintAsSring(self):
        
        number_as_input = -1

        test_string_output = fizz_buzz(number_as_input)

        self.assertEqual(test_string_output, "-1")

    def test_GivenACharacterAsInput_whenFizzBuzzFunctionGetsTheInput_thenTheFunctionFails(self):

        character_as_input = "a"

        test_string_output = fizz_buzz(character_as_input)

        self.assertEqual(test_string_output, "Error: Input should be Integer.")

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


class TestAddNumber(unittest.TestCase):
    """
    AddNumber unittest class
    """

    def test_GivenAnEmptySrtingAsInput_whenAddNumberFunctionGetsTheInput_thenTheFunctionPrintsZero(self):

        string_as_input = []

        test_result = add_number(string_as_input)

        self.assertEqual(test_result, 0)

    def test_GivenAnStringWithOneElement_whenAddNumberFunctionGetsTheInput_thenTheFunctionPrintsTheElement(self):

        string_as_input = [1]

        test_result = add_number(string_as_input)

        self.assertEqual(test_result, 1)

    def test_GivenAnStringWithTwoElements_whenAddNumberFunctionGetsTheInput_thenTheFunctionPrintsTheSumOfTheElements(self):

        string_as_input = [1,2]

        test_result = add_number(string_as_input)

        self.assertEqual(test_result, 3)

    def test_GivenAnUnknownNumberOfElements_whenAddNumberFunctionGetsTheInput_thenTheFunctionPrintsTheSumOfTheElements(self):

        string_as_input = [1,2,3,4,5,6,7,8,9,10]

        test_result = add_number(string_as_input)

        self.assertEqual(test_result, 55)