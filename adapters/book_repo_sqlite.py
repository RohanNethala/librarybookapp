# adapters/book_repo_sqlite.py
import sqlite3
from entities.book import Book

class BookRepoSQLite:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            is_borrowed BOOLEAN
        )""")
        self.conn.commit()

    def create(self, title, author):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO books (title, author, is_borrowed) VALUES (?, ?, ?)",
                       (title, author, False))
        self.conn.commit()
        return Book(cursor.lastrowid, title, author, False)

    def get(self, book_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, title, author, is_borrowed FROM books WHERE id = ?", (book_id,))
        row = cursor.fetchone()
        if row:
            return Book(*row)
        return None

    def update(self, book):
        self.conn.execute(
            "UPDATE books SET title = ?, author = ?, is_borrowed = ? WHERE id = ?",
            (book.title, book.author, book.is_borrowed, book.id)
        )
        self.conn.commit()

    def get_all(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, title, author, is_borrowed FROM books")
        rows = cursor.fetchall()
        return [Book(*row) for row in rows]
