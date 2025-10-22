# -*- coding: utf-8 -*-

"""
TDD Manifesto exercises
"""
import re

def fizz_buzz(num):
    if type(num) == int:
        if num > 0:
            if num % 3 == 0 and num % 5 == 0:
                return "FizzBuzz"
            elif num % 3 == 0:
                return "Fizz"
            elif num % 5 == 0:
                return "Buzz"
            else:
                return str(num)
        else:
            return str(num)
    else:
        return "Error: Input should be Integer."

def add_number(string_input):
    sum_result = 0
    if string_input != "":
        list_of_numbers = re.split(r"[,\n]+", string_input)
        for number in list_of_numbers:
            sum_result += int(number)
    return sum_result