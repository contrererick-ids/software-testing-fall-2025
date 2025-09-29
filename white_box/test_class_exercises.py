# -*- coding: utf-8 -*-

"""
White-box unit testing examples.
"""
import unittest

from white_box.class_exercises import (
    VendingMachine,
    calculate_items_shipping_cost,
    calculate_total_discount,
    calculate_order_total,
    check_number_status,
    divide,
    get_grade,
    is_even,
    is_triangle,
    validate_password
)


class TestWhiteBox(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_is_even_with_even_number(self):
        """
        Checks if a number is even.
        """
        self.assertTrue(is_even(0))

    def test_is_even_with_odd_number(self):
        """
        Checks if a number is not even.
        """
        self.assertFalse(is_even(7))

    def test_divide_by_non_zero(self):
        """
        Checks the divide function works as expected.
        """
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        """
        Checks the divide function returns 0 when dividing by 0.
        """
        self.assertEqual(divide(10, 0), 0)

    def test_get_grade_a(self):
        """
        Checks A grade.
        """
        self.assertEqual(get_grade(95), "A")

    def test_get_grade_b(self):
        """
        Checks B grade.
        """
        self.assertEqual(get_grade(85), "B")

    def test_get_grade_c(self):
        """
        Checks C grade.
        """
        self.assertEqual(get_grade(75), "C")

    def test_get_grade_f(self):
        """
        Checks F grade.
        """
        self.assertEqual(get_grade(65), "F")

    def test_is_triangle_yes(self):
        """
        Checks the three inputs can form a triangle.
        """
        self.assertEqual(is_triangle(3, 4, 5), "Yes, it's a triangle!")

    def test_is_triangle_no_1(self):
        """
        Checks the three inputs can't form a triangle when C is greater or equal than A + B.
        """
        self.assertEqual(is_triangle(3, 4, 7), "No, it's not a triangle.")

    def test_is_triangle_no_2(self):
        """
        Checks the three inputs can't form a triangle when B is greater or equal than A + C.
        """
        self.assertEqual(is_triangle(2, 3, 1), "No, it's not a triangle.")

    def test_is_triangle_no_3(self):
        """
        Checks the three inputs can't form a triangle when A is greater or equal than B + C.
        """
        self.assertEqual(is_triangle(2, 1, 1), "No, it's not a triangle.")


class TestWhiteBoxVendingMachine(unittest.TestCase):
    """
    Vending Machine unit tests.
    """

    # @classmethod
    # def setUpClass(cls):
    #    return

    def setUp(self):
        self.vending_machine = VendingMachine()
        self.assertEqual(self.vending_machine.state, "Ready")

    # def tearDown(self):
    #    return

    # @classmethod
    # def tearDownClass(cls):
    #    return

    def test_vending_machine_insert_coin_error(self):
        """
        Checks the vending machine can accept coins.
        """
        self.vending_machine.state = "Dispensing"

        output = self.vending_machine.insert_coin()

        self.assertEqual(self.vending_machine.state, "Dispensing")
        self.assertEqual(output, "Invalid operation in current state.")

    def test_vending_machine_insert_coin_success(self):
        """
        Checks the vending machine fails to accept coins when it's not ready.
        """
        output = self.vending_machine.insert_coin()

        self.assertEqual(self.vending_machine.state, "Dispensing")
        self.assertEqual(output, "Coin Inserted. Select your drink.")


class TestWhiteBoxCheckNumberStatus(unittest.TestCase):
    """
    Check number status unit tests.
    """

    def test_check_number_status_negative(self):
        """
        Checks the number is negative.
        """
        self.assertEqual(check_number_status(-1), "Negative")

    def test_check_number_status_zero(self):
        """
        Checks the number is zero.
        """
        self.assertEqual(check_number_status(0), "Zero")

    def test_check_number_status_positive(self):
        """
        Checks the number is a positive number.
        """
        self.assertEqual(check_number_status(1), "Positive")


class TestValidatePassword(unittest.TestCase):
    """
    Validate password unit tests.
    """

    def test_validate_password_too_short(self):
        """
        Checks the password is too short.
        """
        self.assertFalse(validate_password("Pass12!"))

    def test_validate_password_no_uppercase(self):
        """
        Checks the password has no uppercase letter.
        """
        self.assertFalse(validate_password("pass1234!"))

    def test_validate_password_no_lowercase(self):
        """
        Checks the password has no lowercase letter.
        """
        self.assertFalse(validate_password("PASS1234!"))

    def test_validate_password_no_digit(self):
        """
        Checks the password has no digit.
        """
        self.assertFalse(validate_password("Password!"))

    def test_validate_password_no_special_char(self):
        """
        Checks the password has no special character.
        """
        self.assertFalse(validate_password("Pass1234"))

    def test_validate_password_valid(self):
        """
        Checks the password is valid.
        """
        self.assertTrue(validate_password("Pass1234!"))


class TestCalculateTotalDiscount(unittest.TestCase):
    """
    Calculate total discount unit tests.
    """

    def test_calculate_total_discount_no_discount(self):
        """
        Checks no discount applied.
        """
        self.assertEqual(calculate_total_discount(99), 0)

    def test_calculate_total_discount_ten_percent(self):
        """
        Checks 10% discount applied.
        """
        self.assertEqual(calculate_total_discount(100), 10)
        self.assertEqual(calculate_total_discount(500), 50)

    def test_calculate_total_discount_twenty_percent(self):
        """
        Checks 20% discount applied.
        """
        self.assertEqual(calculate_total_discount(501), 100.2)


class TestCalculateOrderTotal(unittest.TestCase):
    """
    Calculate order total unit tests.
    """

    def test_calculate_order_total_no_items(self):
        """
        Checks the order total with no items.
        """

        self.assertEqual(calculate_order_total([]), 0)

    def test_calculate_order_total_no_discount(self):
        """
        Checks the order total with no discount.
        """

        items = [{"quantity": 1, "price": 20},
                 {"quantity": 5, "price": 20}
        ]
        self.assertEqual(calculate_order_total(items), 120)

    def test_calculate_order_total_with_five_percent(self):
        """
        Checks the order total with 5% discount.
        """

        items = [{"quantity": 6, "price": 20},
                 {"quantity": 10, "price": 20}
        ]
        self.assertEqual(calculate_order_total(items), 304)

    def test_calculate_order_total_with_ten_percent(self):
        """
        Checks the order total with 10% discount.
        """

        items = [{"quantity": 11, "price": 20}]
        self.assertEqual(calculate_order_total(items), 198)

class TestCalculateItemsShippingCost(unittest.TestCase):
    """
    Calculate items shipping cost unit tests.
    """

    def test_calculate_items_shipping_cost_no_items(self):
        """
        Checks the shipping cost with no items and valid shipping method.
        """

        self.assertEqual(calculate_items_shipping_cost([],"standard"), 10)
        self.assertEqual(calculate_items_shipping_cost([],"express"), 20)
        self.assertRaises(ValueError, calculate_items_shipping_cost, [], "invalid")

    def test_calculate_items_shipping_cost_equals_ten_and_shippoing_method_standard(self):
        """
        Checks the shipping cost with standard shipping method and total weight less than 5.
        """

        items = [{"weight": 1},
                 {"weight": 1},
                 {"weight": 2}
        ]
        self.assertEqual(calculate_items_shipping_cost(items,"standard"), 10)
    
    def test_calculate_items_shipping_cost_equals_fifteen_and_shipping_method_standard(self):
        """
        Checks the shipping cost with standard shipping method and total weight greater than 5.
        """

        items = [{"weight": 3},
                 {"weight": 3}
        ]
        self.assertEqual(calculate_items_shipping_cost(items,"standard"), 15)
        items = [{"weight": 3},
                 {"weight": 2},
                 {"weight": 5}
        ]
        self.assertEqual(calculate_items_shipping_cost(items,"standard"), 15)

    def test_calculate_items_shipping_cost_equals_twenty_and_shipping_method_standard(self):
        """
        Checks the shipping cost with express shipping method and total weight less than 5.
        """

        items = [{"weight": 5},
                 {"weight": 3},
                 {"weight": 3}
        ]
        self.assertEqual(calculate_items_shipping_cost(items,"standard"), 20)

    def test_calculate_items_shipping_cost_equals_twenty_and_shipping_method_expres(self):
        """
        Checks the shipping cost with express shipping method and total weight less than 5.
        """

        items = [{"weight": 1},
                 {"weight": 1},
                 {"weight": 2}
        ]
        self.assertEqual(calculate_items_shipping_cost(items,"express"), 20)
    
    def test_calculate_items_shipping_cost_equals_thirty_and_shipping_method_expres(self):
        """
        Checks the shipping cost with express shipping method and total weight greater than 5.
        """

        items = [{"weight": 3},
                 {"weight": 3}
        ]
        self.assertEqual(calculate_items_shipping_cost(items,"express"), 30)
        items = [{"weight": 3},
                 {"weight": 2},
                 {"weight": 5}
        ]
        self.assertEqual(calculate_items_shipping_cost(items,"express"), 30)
    
    def test_calculate_items_shipping_cost_equals_forty_and_shipping_method_expres(self):
        """
        Checks the shipping cost with express shipping method and total weight greater than 10.
        """

        items = [{"weight": 5},
                 {"weight": 6}
        ]
        self.assertEqual(calculate_items_shipping_cost(items,"express"), 40)

    def test_calculate_items_shipping_cost_invalid_shipping_method(self):
        """
        Checks the shipping cost with invalid shipping method.
        """

        items = [{"weight": 1},
                 {"weight": 1},
                 {"weight": 2}
        ]
        self.assertRaises(ValueError, calculate_items_shipping_cost, items, "invalid")

