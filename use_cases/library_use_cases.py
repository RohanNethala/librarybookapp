# use_cases/library_use_cases.py
class LibraryUseCases:
    def __init__(self, book_repo):
        self.book_repo = book_repo

    def add_book(self, title, author):
        new_book = self.book_repo.create(title, author)
        return new_book

    def borrow_book(self, book_id):
        book = self.book_repo.get(book_id)
        if not book:
            raise ValueError("Book not found")
        if book.is_borrowed:
            raise ValueError("Book is already borrowed")
        book.is_borrowed = True
        self.book_repo.update(book)
        return book

    def list_books(self):
        return self.book_repo.get_all()
