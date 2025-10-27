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
    list_of_numbers = []
    negative_numbers = []
    er_for_custom_separator = r"^//(.+)\n(.*)$"
    match = re.match(er_for_custom_separator, string_input)
    if match:
        custom_separator = match.group(1)
        numbers_part = match.group(2)
        invalid_separator_match = re.search(rf"[^\d{custom_separator}\n]", numbers_part)
        if invalid_separator_match:
            invalid_char = invalid_separator_match.group(0)
            position = invalid_separator_match.start()
            return f"'{custom_separator}' expected but '{invalid_char}' found at position {position}."
        list_of_numbers = re.split(re.escape(custom_separator), numbers_part)
    else:
        er = re.findall(r",\n", string_input)
        if er:
            return "Invalid input"
        if string_input.endswith(","):
            return -1
        if string_input != "":
            list_of_numbers = re.split(r"[,\n]+", string_input)
    for number in list_of_numbers:
        if int(number) < 0:
            negative_numbers.append(number)
    if negative_numbers:
        return f"Negative number(s) not allowed: {', '.join(negative_numbers)}"
    for number in list_of_numbers:
        sum_result += int(number)
    return sum_result
