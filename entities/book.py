# entities/book.py
class Book:
    def __init__(self, id: int, title: str, author: str, is_borrowed: bool = False):
        self.id = id
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
