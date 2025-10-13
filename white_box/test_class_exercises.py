# -*- coding: utf-8 -*-

"""
White-box unit testing examples.
"""
import unittest
from unittest.mock import patch

from white_box.class_exercises import (
    BankAccount,
    BankingSystem,
    Product,
    ShoppingCart,
    TrafficLight,
    VendingMachine,
    calculate_items_shipping_cost,
    calculate_order_total,
    calculate_quantity_discount,
    calculate_total_discount,
    categorize_product,
    celsius_to_fahrenheit,
    check_file_size,
    check_flight_eligibility,
    check_number_status,
    divide,
    get_grade,
    is_even,
    is_triangle,
    validate_credit_card,
    validate_date,
    validate_email,
    validate_login,
    validate_password,
    validate_url,
    verify_age,
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

        items = [{"quantity": 1, "price": 20}, {"quantity": 5, "price": 20}]
        self.assertEqual(calculate_order_total(items), 120)

    def test_calculate_order_total_with_five_percent(self):
        """
        Checks the order total with 5% discount.
        """

        items = [{"quantity": 6, "price": 20}, {"quantity": 10, "price": 20}]
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

        self.assertEqual(calculate_items_shipping_cost([], "standard"), 10)
        self.assertEqual(calculate_items_shipping_cost([], "express"), 20)
        self.assertRaises(ValueError, calculate_items_shipping_cost, [], "invalid")

    def test_calculate_items_shipping_cost_equals_ten_and_shippoing_method_standard(
        self,
    ):
        """
        Checks the shipping cost with standard shipping method and total weight less than 5.
        """

        items = [{"weight": 1}, {"weight": 1}, {"weight": 2}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 10)

    def test_calculate_items_shipping_cost_equals_fifteen_and_shipping_method_standard(
        self,
    ):
        """
        Checks the shipping cost with standard shipping method and total weight greater than 5.
        """

        items = [{"weight": 3}, {"weight": 3}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 15)
        items = [{"weight": 3}, {"weight": 2}, {"weight": 5}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 15)

    def test_calculate_items_shipping_cost_equals_twenty_and_shipping_method_standard(
        self,
    ):
        """
        Checks the shipping cost with express shipping method and total weight less than 5.
        """

        items = [{"weight": 5}, {"weight": 3}, {"weight": 3}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 20)

    def test_calculate_items_shipping_cost_equals_twenty_and_shipping_method_expres(
        self,
    ):
        """
        Checks the shipping cost with express shipping method and total weight less than 5.
        """

        items = [{"weight": 1}, {"weight": 1}, {"weight": 2}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 20)

    def test_calculate_items_shipping_cost_equals_thirty_and_shipping_method_expres(
        self,
    ):
        """
        Checks the shipping cost with express shipping method and total weight greater than 5.
        """

        items = [{"weight": 3}, {"weight": 3}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 30)
        items = [{"weight": 3}, {"weight": 2}, {"weight": 5}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 30)

    def test_calculate_items_shipping_cost_equals_forty_and_shipping_method_expres(
        self,
    ):
        """
        Checks the shipping cost with express shipping method and total weight greater than 10.
        """

        items = [{"weight": 5}, {"weight": 6}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 40)

    def test_calculate_items_shipping_cost_invalid_shipping_method(self):
        """
        Checks the shipping cost with invalid shipping method.
        """

        items = [{"weight": 1}, {"weight": 1}, {"weight": 2}]
        self.assertRaises(ValueError, calculate_items_shipping_cost, items, "invalid")


class TestValidateLogin(unittest.TestCase):
    """
    Validate login unit tests.
    """

    def test_validate_login_empty_username(self):
        """
        Checks the username is empty.
        """

        self.assertEqual(validate_login("", "Password123!"), "Login Failed")

    def test_validate_login_empty_password(self):
        """
        Checks the password is empty.
        """

        self.assertEqual(validate_login("Username", ""), "Login Failed")

    def test_validate_login_invalid_username_length_less_than_five(self):
        """
        Checks the username length is less than five characters.
        """

        self.assertEqual(validate_login("use", "Password123!"), "Login Failed")

    def test_validate_login_invalid_username_length_more_than_twenty(self):
        """
        Checks the username length is greater than twenty characters.
        """

        self.assertEqual(
            validate_login("thisisaverylonguserna", "Password123!"), "Login Failed"
        )

    def test_validate_login_invalid_password_length_less_than_eight(self):
        """
        Checks the password length is less than eight characters.
        """

        self.assertEqual(validate_login("Username", "Pass1!"), "Login Failed")

    def test_validate_login_invalid_password_length_greater_than_fifteen(self):
        """
        Checks the password length is greater than fifteen characters.
        """

        self.assertEqual(validate_login("Username", "Thisisaverylongp"), "Login Failed")

    def test_validate_login_success(self):
        """
        Checks the login is successful.
        """

        self.assertEqual(validate_login("Username", "Password123!"), "Login Successful")


class TestVerifyAge(unittest.TestCase):
    """
    Verify age unit tests.
    """

    def test_verify_age_underage(self):
        """
        Checks the age is underage.
        """

        self.assertEqual(verify_age(17), "Not Eligible")

    def test_verify_age_eigthteen(self):
        """
        Checks the age is of age.
        """

        self.assertEqual(verify_age(18), "Eligible")

    def test_verify_age_sixtyfive(self):
        """
        Checks the age is overage.
        """

        self.assertEqual(verify_age(65), "Eligible")

    def test_verify_age_overage(self):
        """
        Checks the age is overage.
        """

        self.assertEqual(verify_age(66), "Not Eligible")


class TestCategorizeProduct(unittest.TestCase):
    """
    Categorize product unit tests.
    """

    def test_categorize_product_category_a(self):
        """
        Checks the product is in category A.
        """

        self.assertEqual(categorize_product(10), "Category A")
        self.assertEqual(categorize_product(50), "Category A")

    def test_categorize_product_category_b(self):
        """
        Checks the product is in category B.
        """

        self.assertEqual(categorize_product(51), "Category B")
        self.assertEqual(categorize_product(100), "Category B")

    def test_categorize_product_category_c(self):
        """
        Checks the product is in category C.
        """

        self.assertEqual(categorize_product(101), "Category C")
        self.assertEqual(categorize_product(200), "Category C")

    def test_categorize_product_category_d(self):
        """
        Checks the product is in category D.
        """

        self.assertEqual(categorize_product(9), "Category D")
        self.assertEqual(categorize_product(201), "Category D")


class TestValidateEmail(unittest.TestCase):
    """
    Validate email unit tests.
    """

    def test_validate_email_too_short(self):
        """
        Checks the email is too short.
        """

        self.assertEqual(validate_email("a@.b"), "Invalid Email")

    def test_validate_email_no_at_symbol(self):
        """
        Checks the email has no "@" symbol.
        """

        self.assertEqual(validate_email("userexample.com"), "Invalid Email")

    def test_validate_email_no_dot_symbol(self):
        """
        Checks the email has no "." symbol.
        """

        self.assertEqual(validate_email("user@examplecom"), "Invalid Email")

    def test_validate_email_too_long(self):
        """
        Checks the email is too long.
        """

        self.assertEqual(
            validate_email("userthatistoolong@examplethatistoolong.comthatistoolong"),
            "Invalid Email",
        )

    def test_validate_email_valid(self):
        """
        Checks the email is valid.
        """

        self.assertEqual(validate_email("user@example.com"), "Valid Email")


class TestCelsiusToFahrenheit(unittest.TestCase):
    """
    Celsius to Fahrenheit unit tests.
    """

    def test_celsius_to_fahrenheit_freezing(self):
        """
        Checks the conversion of 0 Celsius to Fahrenheit.
        """

        self.assertEqual(celsius_to_fahrenheit(0), 32)

    def test_celsius_to_fahrenheit_grater_than_one_hundred(self):
        """
        Checks the conversion of temperature greater than 100 Celsius to Fahrenheit.
        """

        self.assertEqual(celsius_to_fahrenheit(101), "Invalid Temperature")

    def test_celsius_to_fahrenheit_less_than_negative_one_hundred(self):
        """
        Checks the conversion of temperature less than -100 Celsius to Fahrenheit.
        """

        self.assertEqual(celsius_to_fahrenheit(-101), "Invalid Temperature")

    def test_celsius_to_fahrenheit_equal_one_hundred(self):
        """
        Checks the conversion of 100 Celsius to Fahrenheit.
        """

        self.assertEqual(celsius_to_fahrenheit(100), 212)

    def test_celsius_to_fahrenheit_equal_negative_one_hundred(self):
        """
        Checks the conversion of -100 Celsius to Fahrenheit.
        """

        self.assertEqual(celsius_to_fahrenheit(-100), -148)


class TestTrafficLight(unittest.TestCase):
    """
    Traffic light unit tests.
    """

    def test_traffic_light_initial_state(self):
        """
        Checks the traffic light is red.
        """

        light = TrafficLight()
        self.assertEqual(light.get_current_state(), "Red")

    def test_traffic_light_green(self):
        """
        Checks the traffic light changes to green.
        """

        light = TrafficLight()
        light.change_state()
        self.assertEqual(light.get_current_state(), "Green")

    def test_traffic_light_yellow(self):
        """
        Checks the traffic light changes to yellow.
        """

        light = TrafficLight()
        light.change_state()
        light.change_state()
        self.assertEqual(light.get_current_state(), "Yellow")

    def test_traffic_light_red(self):
        """
        Checks the traffic light changes back to red.
        """

        light = TrafficLight()
        light.change_state()
        light.change_state()
        light.change_state()
        self.assertEqual(light.get_current_state(), "Red")


class TestBankAccount(unittest.TestCase):
    """
    Bank account unit tests.
    """

    def setUp(self):
        self.bank_account = BankAccount("123456", 1000)
        self.assertEqual(self.bank_account.account_number, "123456")
        self.assertEqual(self.bank_account.balance, 1000)

    def test_view_account_details(self):
        """
        Checks the account details are correct.
        """
        bank_account = BankAccount("123456", 1000)

        with patch("white_box.class_exercises.print") as mock_print:
            bank_account.view_account()
        mock_print.assert_called_once_with("The account 123456 has a balance of 1000")


class TestBankingSystem(unittest.TestCase):
    """
    Banking system unit tests.
    """

    def test_init_baking_system(self):
        """
        Checks the banking system is initialized correctly.
        """

        banking_system = BankingSystem()
        self.assertEqual(banking_system.users, {"user123": "pass123"})
        self.assertEqual(banking_system.logged_in_users, set())

    def test_authenticate_user_succesfully(self):
        """
        Checks the user is authenticated successfully.
        """

        banking_system = BankingSystem()
        user = "user123"
        password = "pass123"
        with patch("white_box.class_exercises.print") as mock_print:
            banking_system.authenticate(user, password)
        mock_print.assert_called_once_with("User user123 authenticated successfully.")

    def test_authenticate_user_already_logged_in(self):
        """
        Checks the user alreayd logged in.
        """

        banking_system = BankingSystem()
        user = "user123"
        password = "pass123"
        banking_system.authenticate(user, password)
        with patch("white_box.class_exercises.print") as mock_print:
            banking_system.authenticate(user, password)
        mock_print.assert_called_once_with("User already logged in.")

    def test_authenticate_user_failed(self):
        """
        Checks the user is not authenticated.
        """

        banking_system = BankingSystem()
        user = "user123"
        password = "pass456"
        with patch("white_box.class_exercises.print") as mock_print:
            banking_system.authenticate(user, password)
        mock_print.assert_called_once_with("Authentication failed.")

    def test_transfer_with_user_not_authenticated(self):
        """
        Checks the transfer fails when user is not authenticated.
        """

        banking_system = BankingSystem()
        sender = "user123"
        receiver = "user456"
        amount = 100
        transaction_type = "regular"
        with patch("white_box.class_exercises.print") as mock_print:
            banking_system.transfer_money(sender, receiver, amount, transaction_type)
        mock_print.assert_called_once_with("Sender not authenticated.")

    def test_transfer_with_invalid_transaction_type(self):
        """
        Checks the transfer fails when transaction type is invalid.
        """

        banking_system = BankingSystem()
        sender = "user123"
        banking_system.authenticate(sender, "pass123")
        receiver = "user456"
        amount = 100
        transaction_type = "x"
        with patch("white_box.class_exercises.print") as mock_print:
            banking_system.transfer_money(sender, receiver, amount, transaction_type)
        mock_print.assert_called_once_with("Invalid transaction type.")

    def test_transfer_with_insufficient_funds(self):
        """
        Checks the transfer fails when sender has insufficient funds.
        """

        banking_system = BankingSystem()
        sender = "user123"
        banking_system.authenticate(sender, "pass123")
        receiver = "user456"
        amount = 2000
        transaction_type = "regular"
        with patch("white_box.class_exercises.print") as mock_print:
            banking_system.transfer_money(sender, receiver, amount, transaction_type)
        mock_print.assert_called_once_with("Insufficient funds.")

    def test_transfer_succesfully_regular(self):
        """
        Checks the transfer is successful with regular transaction type.
        """

        banking_system = BankingSystem()
        sender = "user123"
        banking_system.authenticate(sender, "pass123")
        receiver = "user456"
        amount = 100
        transaction_type = "regular"
        with patch("white_box.class_exercises.print") as mock_print:
            banking_system.transfer_money(sender, receiver, amount, transaction_type)
        mock_print.assert_called_once_with(
            f"Money transfer of ${amount} ({transaction_type} transfer)"
            f" from {sender} to {receiver} processed successfully."
        )

    def test_transfer_succesfully_express(self):
        """
        Checks the transfer is successful with express transaction type.
        """

        banking_system = BankingSystem()
        sender = "user123"
        banking_system.authenticate(sender, "pass123")
        receiver = "user456"
        amount = 100
        transaction_type = "express"
        with patch("white_box.class_exercises.print") as mock_print:
            banking_system.transfer_money(sender, receiver, amount, transaction_type)
        mock_print.assert_called_once_with(
            f"Money transfer of ${amount} ({transaction_type} transfer)"
            f" from {sender} to {receiver} processed successfully."
        )

    def test_transfer_succesfully_scheduled(self):
        """
        Checks the transfer is successful with scheduled transaction type.
        """

        banking_system = BankingSystem()
        sender = "user123"
        banking_system.authenticate(sender, "pass123")
        receiver = "user456"
        amount = 100
        transaction_type = "scheduled"
        with patch("white_box.class_exercises.print") as mock_print:
            banking_system.transfer_money(sender, receiver, amount, transaction_type)
        mock_print.assert_called_once_with(
            f"Money transfer of ${amount} ({transaction_type} transfer)"
            f" from {sender} to {receiver} processed successfully."
        )


class TestProduct(unittest.TestCase):
    """
    Product unit tests.
    """

    def test_init_product(self):
        """
        Checks the product is initialized correctly.
        """

        product = Product("Laptop", 999.99)
        self.assertEqual(product.name, "Laptop")
        self.assertEqual(product.price, 999.99)

    def test_view_product(self):
        """
        Checks the product details are correct.
        """

        product = Product("Laptop", 999.99)
        with patch("white_box.class_exercises.print") as mock_print:
            product.view_product()
        mock_print.assert_called_once_with("The product Laptop has a price of 999.99")


class TestShoppingCart(unittest.TestCase):
    """
    Shopping cart unit tests.
    """

    def test_init_shopping_cart(self):
        """
        Checks the shopping cart is initialized correctly.
        """

        cart = ShoppingCart()
        self.assertEqual(cart.items, [])

    def test_add_product(self):
        """
        Checks a product is added to the shopping cart.
        """

        cart = ShoppingCart()
        product = Product("Laptop", 999.99)
        cart.add_product(product, 1)
        self.assertEqual(len(cart.items), 1)
        self.assertEqual(cart.items[0]["product"], product)
        self.assertEqual(cart.items[0]["quantity"], 1)

    def test_product_already_in_shopping_cart(self):
        """
        Checks a product that is already in the shopping cart is not added again.
        """

        cart = ShoppingCart()
        product = Product("Laptop", 999.99)
        cart.add_product(product, 1)
        cart.add_product(product, 1)
        self.assertEqual(len(cart.items), 1)
        self.assertEqual(cart.items[0]["product"], product)
        self.assertEqual(cart.items[0]["quantity"], 2)

    def test_remove_product(self):
        """
        Checks a product is removed totally from the shopping cart.
        """

        cart = ShoppingCart()
        product = Product("Laptop", 999.99)
        cart.add_product(product, 1)
        cart.remove_product(product)
        self.assertEqual(len(cart.items), 0)

    def test_decrease_product_quantity(self):
        """
        Checks a product quantity is decreased in the shopping cart.
        """

        cart = ShoppingCart()
        product = Product("Laptop", 999.99)
        cart.add_product(product, 2)
        cart.remove_product(product)
        self.assertEqual(len(cart.items), 1)
        self.assertEqual(cart.items[0]["product"], product)
        self.assertEqual(cart.items[0]["quantity"], 1)

    def test_view_cart(self):
        """
        Checks the shopping cart details are correct.
        """

        cart = ShoppingCart()
        product = Product("Laptop", 999.99)
        cart.add_product(product, 1)
        for item in cart.items:
            with patch("white_box.class_exercises.print") as mock_print:
                cart.view_cart()
            mock_print.assert_called_once_with(
                f"{item['quantity']} x {item['product'].name}"
                f" - ${item['product'].price * item['quantity']}"
            )

    def test_checkout(self):
        """
        Checks the checkout total is correct.
        """

        cart = ShoppingCart()
        product1 = Product("Laptop", 999.99)
        product2 = Product("Mouse", 49.99)
        cart.add_product(product1, 1)
        cart.add_product(product2, 2)
        with patch("white_box.class_exercises.print") as mock_print:
            cart.checkout()

        self.assertEqual(mock_print.call_count, 2)

        mock_print.assert_has_calls(
            [
                unittest.mock.call(f"Total: ${999.99 + 2 * 49.99}"),
                unittest.mock.call("Checkout completed. Thank you for shopping!"),
            ]
        )


class TestValidateCreditCard(unittest.TestCase):
    """
    Validate credit card unit tests.
    """

    def test_validate_credit_card_too_short(self):
        """
        Validates error message for credit card number that is too short.
        """

        self.assertEqual(validate_credit_card("123456789012"), "Invalid Card")

    def test_validate_credit_card_too_long(self):
        """
        Validates error message for credit card number that is too long.
        """

        self.assertEqual(validate_credit_card("12345678901234567"), "Invalid Card")

    def test_validate_credit_card_success(self):
        """
        Validates success message for valid credit card number.
        """

        self.assertEqual(validate_credit_card("1234567890123"), "Valid Card")

    def test_validate_credit_card_non_digit_characters(self):
        """
        Validates error message for credit card number with non-digit characters.
        """

        self.assertEqual(validate_credit_card("1234abcd56789"), "Invalid Card")


class TestValidateDate(unittest.TestCase):
    """
    Validate date unit tests.
    For this exercise, we are not considering unexisting dates like February 30, etc.
    """

    def test_validate_date_out_of_range_day(self):
        """
        Validates error message for date with out-of-range day.
        """

        self.assertEqual(validate_date(2000, 1, 32), "Invalid Date")

    def test_validate_date_out_of_range_month(self):
        """
        Validates error message for date with out-of-range month.
        """

        self.assertEqual(validate_date(2000, 13, 1), "Invalid Date")

    def test_validate_date_out_of_range_year(self):
        """
        Validates error message for date with out-of-range year.
        """

        self.assertEqual(validate_date(1899, 1, 1), "Invalid Date")


class TestCheckFlightEligibility(unittest.TestCase):
    """
    Check flight eligibility unit tests.
    """

    def test_passenger_underage_and_frequent_flyer(self):
        """
        Checks the passenger is underage and frequent flyer.
        """

        self.assertEqual(check_flight_eligibility(17, True), "Eligible to Book")

    def test_passenger_overage_and_frequent_flyer(self):
        """
        Checks the passenger is overage and frequent flyer.
        """

        self.assertEqual(check_flight_eligibility(66, True), "Eligible to Book")

    def test_passenger_of_age_eighteen_and_not_frequent_flyer(self):
        """
        Checks the passenger is of age and not a frequent flyer.
        """

        self.assertEqual(check_flight_eligibility(18, False), "Eligible to Book")

    def test_passenger_of_age_sixtyfive_and_not_frequent_flyer(self):
        """
        Checks the passenger is of age and not a frequent flyer.
        """

        self.assertEqual(check_flight_eligibility(65, False), "Eligible to Book")

    def test_passenger_of_age_and_frequent_flyer(self):
        """
        Checks the passenger is of age and a frequent flyer.
        """

        self.assertEqual(check_flight_eligibility(30, True), "Eligible to Book")

    def test_passenger_underage_and_not_frequent_flyer(self):
        """
        Checks the passenger is underage and not frequent flyer.
        """

        self.assertEqual(check_flight_eligibility(17, False), "Not Eligible to Book")

    def test_passenger_overage_and_not_frequent_flyer(self):
        """
        Checks the passenger is overage and not frequent flyer.
        """

        self.assertEqual(check_flight_eligibility(66, False), "Not Eligible to Book")


class TestValidateURL(unittest.TestCase):
    """
    Validate URL unit tests.
    For this exercise, we are considering a URL that starts with http:// should be at maximum
    255 characters long, and a URL that starts with https:// should not have an exceeding length.
    """

    def test_url_too_long(self):
        """
        Validates success and failed case for URL that is too long.
        """

        self.assertEqual(
            validate_url(
                "http://abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmno"
            ),
            "Invalid URL",
        )

    def test_url_starting_http(self):
        """
        Validates success case for URL starting with http://.
        """

        self.assertEqual(validate_url("http://example.com"), "Valid URL")

    def test_url_starting_https(self):
        """
        Validates success case for URL starting with https://.
        """

        self.assertEqual(validate_url("https://example.com"), "Valid URL")


class TestCalculateQuantityDiscount(unittest.TestCase):
    """
    Calculate quantity discount unit tests.
    For this exercise we are not considering that is possible to have 0
    or negative quantities of a product.
    """

    def test_calculate_discount_with_five_items_or_less(self):
        """
        Validates no discount is applied with 5 items or less.
        """

        self.assertEqual(calculate_quantity_discount(5), "No Discount")
        self.assertEqual(calculate_quantity_discount(1), "No Discount")

    def test_calculate_discount_with_six_to_ten_items(self):
        """
        Validates 5% discount is applied with 6 to 10 items.
        """

        self.assertEqual(calculate_quantity_discount(6), "5% Discount")
        self.assertEqual(calculate_quantity_discount(10), "5% Discount")

    def test_calculate_discount_with_eleven_or_more_items(self):
        """
        Validates 10% discount is applied with 11 or more items.
        """

        self.assertEqual(calculate_quantity_discount(11), "10% Discount")
        self.assertEqual(calculate_quantity_discount(20), "10% Discount")


class TestCheckFileSize(unittest.TestCase):
    """
    Check file size unit tests.
    """

    def test_check_file_size_equal_zero(self):
        """
        Checks the file size is equal to zero.
        """

        self.assertEqual(check_file_size(0), "Valid File Size")

    def test_check_file_size_equal_maximum_limit(self):
        """
        Checks the file size is equal to the maximum limit.
        """

        self.assertEqual(check_file_size(1048576), "Valid File Size")

    def test_check_file_size_above_maximum_limit(self):
        """
        Checks the file size is above the maximum limit.
        """

        self.assertEqual(check_file_size(1048577), "Invalid File Size")

    def test_check_file_size_for_negative_values(self):
        """
        Checks the file size is below zero.
        """

        self.assertEqual(check_file_size(-1), "Invalid File Size")
