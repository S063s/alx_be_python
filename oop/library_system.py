class Book:
    def __init__(self, title , author):
        self.title = title
        self.author = author
        
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size 
        def __str__(self):
            return f"{self.title} by {self.author}, {self.file_size}MB"


class PrintBook(Book):
    def __init__(self, title, author, num_pages):
        super().__init__(title, author)
        self.page_count = page_count  

        def __str__(self):
            return f"{self.title} by {self.author}, {self.page_count} pages"        


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book , Ebook , printbook)
        if isinstance(book, EBook):
            print(f"Added eBook: {book.title}")
        elif isinstance(book, PrintBook):
            print(f"Added PrintBook: {book.title}")

    def list_books(self):
        for book in self.books:
            print(f"{book.title} by {book.author}")      