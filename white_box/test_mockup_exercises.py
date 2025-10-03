# -*- coding: utf-8 -*-

"""
Mock up testing examples.
"""
import unittest
from unittest.mock import patch

from white_box.mockup_exercises import fetch_data_from_api, read_data_from_file


class TestDataFetcher(unittest.TestCase):
    """
    Data fetcher unittest class.
    """

    @patch("white_box.mockup_exercises.requests.get")
    def test_fetch_data_from_api_success(self, mock_get):
        """
        Success case.
        """
        # Set up the mock response
        mock_get.return_value.json.return_value = {"key": "value"}

        # Mock the requests.get method
        # with patch("requests.get") as mock_get:
        #     mock_get.return_value.status_code = 200
        #     mock_get.return_value.json.return_value = [
        #         {"id": 1, "title": "Title 1", "body": "Body 1"},
        #         {"id": 2, "title": "Title 2", "body": "Body 2"},
        #     ]

        # mock_get = patch('requests.get')
        # mock_get.return_value.status_code = 200
        # mock_get.return_value.json.return_value = [
        #     {"id": 1, "title": "Title 1", "body": "Body 1"},
        #     {"id": 2, "title": "Title 2", "body": "Body 2"},
        # ]

        # Call the function under test
        result = fetch_data_from_api("https://api.example.com/data")

        # Assert that the function returns the expected result
        self.assertEqual(result, {"key": "value"})

        # Assert that requests.get was called with the correct URL
        mock_get.assert_called_once_with("https://api.example.com/data", timeout=10)


# class TestPrint(unittest.TestCase):
#     """
#     fetch_data_from_api unittest class.
#     """
#
#     def test_print(self):
#         # Mock the requests.get method
#         mock_print = patch('__main__.print')
#
#         print_hello_world()
#
#         # Verify data is what we expect
#         mock_print.assert_called_once_with("Hello, World!")


class TestReadDataFromFile(unittest.TestCase):
    """
    Read data from file unittest class.
    """

    @patch("builtins.open", create=True)
    def test_read_data_from_file_success(self, mock_open):
        """
        Success case.
        """
        # Set up the mock file object
        mock_file = mock_open.return_value.__enter__.return_value

        # Define the content to be returned when the file is read
        mock_file.read.return_value = "Sample data from file."

        # Call the function under test
        result = read_data_from_file("sample.txt")

        # Assert that the function returns the expected result
        self.assertEqual(result, "Sample data from file.")

        # Assert that open was called with the correct filename and encoding
        mock_open.assert_called_once_with("sample.txt", encoding="utf-8")
