class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, book):
        if book in self._books and not book.is_checked_out:
            book.is_checked_out = True
            return True
        return False

    def return_book(self):
        if book in self._books and book.is_checked_out:
            book.is_checked_out = False
            return True
        return False
       

    def list_available_books(self):
        return [book for book in self._books if not book.is_checked_out]
