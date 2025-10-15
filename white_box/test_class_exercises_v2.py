# -*- coding: utf-8 -*-

"""
White-box unit testing examples continuation.
"""
import unittest

from white_box.class_exercises import (
    UserAuthentication,
    authenticate_user,
    calculate_quantity_discount,
    calculate_shipping_cost,
    check_file_size,
    check_flight_eligibility,
    check_loan_eligibility,
    get_weather_advisory,
    grade_quiz,
    validate_url,
)


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


class TestLoanEligibility(unittest.TestCase):
    """
    Loan eligibility unit tests.
    """

    def test_income_less_than_minimum(self):
        """
        Checks the income is less than the minimum required.
        """

        self.assertEqual(check_loan_eligibility(29999, 700), "Not Eligible")

    def test_income_equal_minimum_and_credit_score_below_or_equal_seven_hundred(self):
        """
        Checks the income is equal 30000 and
        the credit score is below or equal 700.
        """

        self.assertEqual(check_loan_eligibility(30000, 700), "Secured Loan")

    def test_income_equal_minimum_and_credit_score_above_seven_hundred(self):
        """
        Checks the income is equal 30000 and
        the credit score is above 700.
        """

        self.assertEqual(check_loan_eligibility(30000, 701), "Standard Loan")

    def test_income_equal_maximum_and_credit_score_below_or_equal_seven_hundred(self):
        """
        Checks the income is equal 60000 and
        the credit score is below or equal 700.
        """

        self.assertEqual(check_loan_eligibility(60000, 700), "Secured Loan")

    def test_income_equal_maximum_and_credit_score_above_seven_hundred(self):
        """
        Checks the income is equal 60000 and
        the credit score is above 700.
        """

        self.assertEqual(check_loan_eligibility(60000, 701), "Standard Loan")

    def test_income_above_maximum_and_credit_score_below_or_equal_seventy_five_hundred(
        self,
    ):
        """
        Checks the income is above 60000 and
        the credit score is below or equal 750.
        """

        self.assertEqual(check_loan_eligibility(60001, 750), "Standard Loan")

    def test_income_above_maximum_and_credit_score_above_seventy_five_hundred(self):
        """
        Checks the income is above 60000 and
        the credit score is above 750.
        """

        self.assertEqual(check_loan_eligibility(60001, 751), "Premium Loan")


class TestCalculateShippingCost(unittest.TestCase):
    """
    Calculate shipping cost unit tests.
    For the following tests, we are not considering floating point values for weight
    and dimensions.
    """

    def test_shipping_cost_equals_five_with_maximum_dimensions(self):
        """
        Checks the shipping cost when dimensions are at maximum limits for the
        shipping cost equals five case.
        """

        weight = 1
        length = 10
        width = 10
        height = 10
        self.assertEqual(calculate_shipping_cost(weight, length, width, height), 5)

    def test_shipping_cost_equals_five_with_minimum_dimensions(self):
        """
        Checks the shipping cost when dimensions are at minimum limits for the
        shipping cost equals five case.
        """

        weight = 1
        length = 1
        width = 1
        height = 1
        self.assertEqual(calculate_shipping_cost(weight, length, width, height), 5)

    def test_shipping_cost_equals_ten_with_maximum_dimensions_and_maximum_weight(self):
        """
        Checks the shipping cost when dimensions and weight are at maximum limits for the
        shipping cost equals ten case.
        """

        weight = 5
        length = 30
        width = 30
        height = 30
        self.assertEqual(calculate_shipping_cost(weight, length, width, height), 10)

    def test_shipping_cost_equals_ten_with_maximum_dimensions_and_minimum_weight(self):
        """
        Checks the shipping cost when dimensions are at maximum limits and weight
        is at minimum limit for the shipping cost equals ten case.
        """

        weight = 2
        length = 30
        width = 30
        height = 30
        self.assertEqual(calculate_shipping_cost(weight, length, width, height), 10)

    def test_shipping_cost_equals_ten_with_minimum_dimensions_and_maximum_weight(self):
        """
        Checks the shipping cost when dimensions are at minimum limits and weight
        is at maximum limit for the shipping cost equals ten case.
        """

        weight = 5
        length = 11
        width = 11
        height = 11
        self.assertEqual(calculate_shipping_cost(weight, length, width, height), 10)

    def test_shipping_cost_equals_ten_with_minimum_dimensions_and_minimum_weight(self):
        """
        Checks the shipping cost when dimensions and weight are at minimum limits for the
        shipping cost equals ten case.
        """

        weight = 2
        length = 11
        width = 11
        height = 11
        self.assertEqual(calculate_shipping_cost(weight, length, width, height), 10)

    def test_shipping_cost_equals_twenty_with_dimensions_above_maximum_in_the_first_scenario(
        self,
    ):
        """
        Checks the shipping cost when dimensions are above maximum limits in the first scenario
        for the shipping cost equals twenty case.
        """

        weight = 1
        length = 11
        width = 11
        height = 11
        self.assertEqual(calculate_shipping_cost(weight, length, width, height), 20)

    def test_shipping_cost_equals_twenty_with_dimensions_above_maximum_in_the_second_scenario(
        self,
    ):
        """
        Checks the shipping cost when dimensions are above maximum limits in the second scenario
        for the shipping cost equals twenty case.
        """

        weight = 5
        length = 31
        width = 31
        height = 31
        self.assertEqual(calculate_shipping_cost(weight, length, width, height), 20)

    def test_shipping_cost_equals_twenty_with_weight_above_maximum(self):
        """
        Checks the shipping cost when weight is above maximum limit
        for the shipping cost equals twenty case.
        """

        weight = 6
        length = 11
        width = 11
        height = 11
        self.assertEqual(calculate_shipping_cost(weight, length, width, height), 20)

    def test_shipping_cost_equals_twenty_with_all_parameters_above_maximum(self):
        """
        Checks the shipping cost when all parameters are above maximum limits
        for the shipping cost equals twenty case.
        """

        weight = 6
        length = 31
        width = 31
        height = 31
        self.assertEqual(calculate_shipping_cost(weight, length, width, height), 20)


class TestGradeQuiz(unittest.TestCase):
    """
    Grade quiz unit tests.
    """

    def test_pass_case(self):
        """
        Validates the pass case.
        """

        correct_answers = 7
        incorrect_answers = 2
        self.assertEqual(grade_quiz(correct_answers, incorrect_answers), "Pass")

    def test_conditional_pass_case(self):
        """
        Validates the conditional pass case.
        """

        correct_answers = 5
        incorrect_answers = 3
        self.assertEqual(
            grade_quiz(correct_answers, incorrect_answers), "Conditional Pass"
        )

    def test_fail_case_with_four_correct_answers(self):
        """
        Validates the fail case.
        """

        correct_answers = 4
        incorrect_answers = 1
        self.assertEqual(grade_quiz(correct_answers, incorrect_answers), "Fail")

    def test_fail_case_with_four_incorrect_answers(self):
        """
        Validates the fail case.
        """

        correct_answers = 7
        incorrect_answers = 4
        self.assertEqual(grade_quiz(correct_answers, incorrect_answers), "Fail")


class TestAuthenticateUser(unittest.TestCase):
    """
    Authenticate user unit tests.
    """

    def test_authenticate_user_as_admin(self):
        """
        Validates the user is authenticated as admin.
        """

        username = "admin"
        password = "admin123"
        self.assertEqual(authenticate_user(username, password), "Admin")

    def test_authenticate_user_as_regular_user(self):
        """
        Validates the user is authenticated as regular user.
        """

        username = "user1"
        password = "pass1238"
        self.assertEqual(authenticate_user(username, password), "User")

    def test_authenticate_user_with_invalid_username(self):
        """
        Validates the user authentication fails due to invalid username.
        """

        username = "user"
        password = "pass1234"
        self.assertEqual(authenticate_user(username, password), "Invalid")

    def test_authenticate_user_with_invalid_password(self):
        """
        Validates the user authentication fails due to invalid password.
        """

        username = "user1"
        password = "pass123"
        self.assertEqual(authenticate_user(username, password), "Invalid")


class TestGetWeatherAdvisory(unittest.TestCase):
    """
    Get weather advisory unit tests.
    For the following exercise, we are not considering floating point values for temperature
    and humidity.
    """

    def test_get_stay_hydrated_advisory(self):
        """
        Validates the advisory to stay hydrated.
        """

        temperature = 31
        humidity = 71
        self.assertEqual(
            get_weather_advisory(temperature, humidity),
            "High Temperature and Humidity. Stay Hydrated.",
        )

    def test_get_bundle_up_advisory(self):
        """
        Validates the advisory to bundle up.
        """

        temperature = -1
        humidity = 71
        self.assertEqual(
            get_weather_advisory(temperature, humidity), "Low Temperature. Bundle Up!"
        )

    def test_temperature_equal_zero(self):
        """
        Validates the advisory when temperature is equal to 0.
        """

        temperature = 0
        humidity = 71
        self.assertEqual(
            get_weather_advisory(temperature, humidity), "No Specific Advisory"
        )

    def test_temperature_below_thirty(self):
        """
        Validates the advisory when temperature is below 30.
        """

        temperature = 29
        humidity = 71
        self.assertEqual(
            get_weather_advisory(temperature, humidity), "No Specific Advisory"
        )

    def test_temperature_above_thirty_but_humidity_below_seventy(self):
        """
        Validates the advisory when temperature is above 30 but humidity is below 70.
        """

        temperature = 31
        humidity = 69
        self.assertEqual(
            get_weather_advisory(temperature, humidity), "No Specific Advisory"
        )


class TestUserAuthentication(unittest.TestCase):
    """
    User authentication unit tests.
    """

    def test_set_up(self):
        """
        Setup method to test user initialization.
        """

        user = UserAuthentication()
        self.assertEqual(user.state, "Logged Out")

    def test_login_successful(self):
        """
        Tests successful login.
        """

        user = UserAuthentication()
        user.login()
        self.assertEqual(user.state, "Logged In")

    def test_login_failed(self):
        """
        Tests failed login.
        """

        user = UserAuthentication()
        user.state = "Logged In"
        self.assertEqual(user.login(), "Invalid operation in current state")

    def test_logout_successful(self):
        """
        Tests successful logout.
        """

        user = UserAuthentication()
        user.login()
        user.logout()
        self.assertEqual(user.state, "Logged Out")

    def test_logout_failed(self):
        """
        Tests failed logout.
        """

        user = UserAuthentication()
        self.assertEqual(user.logout(), "Invalid operation in current state")
