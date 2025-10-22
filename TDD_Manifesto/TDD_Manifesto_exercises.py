# -*- coding: utf-8 -*-

"""
TDD Manifesto exercises
"""

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