# -*- coding: utf-8 -*-

"""
Book store unit testing examples.
"""
import unittest
from unittest.mock import patch

from white_box.book_store import Book, BookStore


class TestBook(unittest.TestCase):
    """
    Book unittest class.
    """

    def setUp(self):
        """
        Creates the book properties
        """
        self.title = "title"
        self.author = "author"
        self.price = 9.99
        self.quantity = 5

    def test_book_init(self):
        """
        Checks the book properties.
        """
        book = Book(self.title, self.author, self.price, self.quantity)
        self.assertEqual(book.title, self.title)
        self.assertEqual(book.author, self.author)
        self.assertEqual(book.price, self.price)
        self.assertEqual(book.quantity, self.quantity)

    @patch("builtins.print")
    def test_book_display(self, mock_print):
        """
        Checks the book display function.
        """
        book = Book(self.title, self.author, self.price, self.quantity)
        book.display()
        self.assertTrue(mock_print.called)
        self.assertEqual(mock_print.call_count, 4)
        mock_print.assert_any_call(f"Title: {self.title}")
        mock_print.assert_called_with(f"Quantity: {self.quantity}")


class TestBookStore(unittest.TestCase):
    """
    Book store unittest class.
    """

    def test_book_store_init(self):
        """
        Checks the book store properties.
        """
        book_store = BookStore()
        self.assertEqual(book_store.books, [])

    @patch("builtins.print")
    def test_add_book(self, mock_print):
        """
        Test the add_book function to append a book to the BookStore array.
        """

        title = "1984"
        author = "George Orwell"
        price = 3.5
        quantity = 2
        book = Book(title, author, price, quantity)
        book_store = BookStore()
        book_store.add_book(book)
        mock_print.assert_any_call(f"Book '{book.title}' added to the store.")

    @patch("builtins.print")
    def test_display_books_in_book_store_no_empty_array(self, mock_print):
        """
        Test the display_books function to print all the books in the array
        when it's not empty.
        """

        title = "1984"
        author = "George Orwell"
        price = 3.5
        quantity = 2
        book = Book(title, author, price, quantity)
        book_store = BookStore()
        book_store.add_book(book)
        book_store.display_books()
        mock_print.assert_has_calls(
            [
                unittest.mock.call(f"Title: {book.title}"),
                unittest.mock.call(f"Author: {book.author}"),
                unittest.mock.call(f"Price: ${book.price}"),
                unittest.mock.call(f"Quantity: {book.quantity}"),
            ]
        )

    @patch("builtins.print")
    def test_display_books_in_book_store_with_empty_array(self, mock_print):
        """
        Test the display_books function to print all the books in the array
        when it's empty.
        """

        book_store = BookStore()
        book_store.display_books()
        mock_print.assert_any_call("No books in the store.")

    @patch("builtins.print")
    def test_search_book_with_empty_array(self, mock_print):
        """
        Test the search_book function with an empty array.
        """

        title = "1984"
        book_store = BookStore()
        book_store.search_book(title)
        mock_print.assert_any_call(f"No book found with title '{title}'.")

    @patch("builtins.print")
    def test_search_book_with_no_empty_array_and_title_exists(self, mock_print):
        """
        Test the search_book function with no empty array and the title exists.
        """

        title = "1984"
        author = "George Orwell"
        price = 3.5
        quantity = 2
        book = Book(title, author, price, quantity)
        book_store = BookStore()
        book_store.add_book(book)
        book_store.search_book(title)
        found_count = len(
            [book for book in book_store.books if book.title.lower() == title.lower()]
        )
        mock_print.assert_has_calls(
            [
                unittest.mock.call(
                    f"Found {found_count} book(s) with title '{title}':"
                ),
                unittest.mock.call(f"Title: {book.title}"),
                unittest.mock.call(f"Author: {book.author}"),
                unittest.mock.call(f"Price: ${book.price}"),
                unittest.mock.call(f"Quantity: {book.quantity}"),
            ]
        )

    @patch("builtins.print")
    def test_search_book_with_no_empty_array_and_title_does_not_exists(
        self, mock_print
    ):
        """
        Test the search_book function with no empty array and the title does not exists.
        """

        title = "1984"
        author = "George Orwell"
        price = 3.5
        quantity = 2
        book = Book(title, author, price, quantity)
        book_store = BookStore()
        book_store.add_book(book)
        title_to_search = "Farenheit 451"
        book_store.search_book(title_to_search)
        found_count = len(
            [
                book
                for book in book_store.books
                if book.title.lower() == title_to_search.lower()
            ]
        )
        mock_print.assert_any_call(f"No book found with title '{title_to_search}'.")
