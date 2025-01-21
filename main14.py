# Задача 1: Тестирование класса с использованием pytest

class InsufficientFundsError(Exception):
    def __init__(self):
        super().__init__("Недостаточно средств на счете.")

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма депозита должна быть положительной.")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError()
        self.balance -= amount

    def get_balance(self):
        return self.balance


# Задача 2: Тестирование класса с использованием unittest

class BookNotFoundError(Exception):
    def __init__(self):
        super().__init__("Книга не найдена в библиотеке.")

class Library:
    def __init__(self):
        self.books = set()

    def add_book(self, title):
        self.books.add(title)

    def remove_book(self, title):
        if title not in self.books:
            raise BookNotFoundError()
        self.books.remove(title)

    def list_books(self):
        return list(self.books)


# Задача 3: Тестирование класса с использованием doctest

class Rectangle:
    def __init__(self, width=0, height=0):
        """
        Инициализация прямоугольника с заданными шириной и высотой.
        >>> r = Rectangle(3, 4)
        >>> r.get_area()
        12
        >>> r.get_perimeter()
        14
        """
        self.width = width
        self.height = height

    def set_dimensions(self, width, height):
        """
        Устанавливает ширину и высоту прямоугольника.
        >>> r = Rectangle()
        >>> r.set_dimensions(6, 7)
        >>> r.get_area()
        42
        >>> r.get_perimeter()
        26
        """
        if width <= 0 or height <= 0:
            raise ValueError("Ширина и высота должны быть положительными числами.")
        self.width = width
        self.height = height

    def get_area(self):
        """Возвращает площадь прямоугольника."""
        return self.width * self.height

    def get_perimeter(self):
        """Возвращает периметр прямоугольника."""
        return 2 * (self.width + self.height)


# Тестирование с использованием pytest для BankAccount

import pytest

@pytest.fixture
def bank_account():
    return BankAccount(100)

def test_initial_balance(bank_account):
    assert bank_account.get_balance() == 100

def test_deposit(bank_account):
    bank_account.deposit(50)
    assert bank_account.get_balance() == 150

def test_withdraw(bank_account):
    bank_account.withdraw(30)
    assert bank_account.get_balance() == 70

def test_withdraw_insufficient_funds(bank_account):
    with pytest.raises(InsufficientFundsError):
        bank_account.withdraw(200)

def test_deposit_negative_amount(bank_account):
    with pytest.raises(ValueError):
        bank_account.deposit(-10)


# Тестирование с использованием unittest для Library

import unittest

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()

    def test_add_book(self):
        self.library.add_book("1984")
        self.assertIn("1984", self.library.list_books())

    def test_remove_book(self):
        self.library.add_book("Brave New World")
        self.library.remove_book("Brave New World")
        self.assertNotIn("Brave New World", self.library.list_books())

    def test_remove_nonexistent_book(self):
        with self.assertRaises(BookNotFoundError):
            self.library.remove_book("Nonexistent Book")

if __name__ == '__main__':
    unittest.main()


# Тестирование с использованием doctest для Rectangle

import doctest

if __name__ == "__main__":
    doctest.testmod()
