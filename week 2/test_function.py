import pytest
from library import Library
from book import Book


def test_add_book():
    book = Book(title="jfk", author="fkj")
    library = Library()
    library.add_book(book)
    assert book in library.books


def test_empty_values():
    library = Library()
    book = Book(title="", author="")
    library.add_book(book)
    assert book not in library.books

def test_special_notes():
    library = Library()
    book = Book(title="@hdj./*", author="hj`nk`w'")
    library.add_book(book)
    assert book in library.books

def test_check_out_book():
    library = Library()
    username = "Moshe"
    book = Book(title="hjk0", author="j")
    library.add_user(username)
    library.add_book(book)
    library.check_out_book(username, book)
    assert library.checked_out_books[username] == book

def test_return_book():
    library = Library()
    book = Book(title="hjk0", author="hjjhkj0")
    library.add_book(book)
    library.add_user("Moshe")
    library.check_out_book("Moshe", book)
    library.return_book("Moshe", book)
    assert book.is_checked_out == False
    assert "Moshe" not in library.checked_out_books


# def test_book_does_not_exist():
#     book = Book(title="sh", author="dh")
#     library = Library()
#     library.add_user("Moshe")
#     assert library.check_out_book("Moshe",book)


def test_book_does_not_exist():
    book = Book(title="sh", author="dh")
    library = Library()
    library.add_user("Moshe")
    with pytest.raises(ValueError) as excinfo:
        library.check_out_book("Moshe", book)
    assert str(excinfo.value) == f"Book '{book.title}' by {book.author} is not in the library."

