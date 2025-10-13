# -*- coding: utf-8 -*-

"""
White-box unit testing examples continuation.
"""
import unittest

from white_box.class_exercises import (
    calculate_quantity_discount,
    check_file_size,
    check_flight_eligibility,
    check_loan_eligibility,
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
