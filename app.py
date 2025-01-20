# app.py
from flask import Flask, jsonify, request
from adapters.book_repo_sqlite import BookRepoSQLite
from use_cases.library_use_cases import LibraryUseCases

app = Flask(__name__)

# Initialize repository and use cases
book_repo = BookRepoSQLite(db_path="library.db")
library_use_cases = LibraryUseCases(book_repo)

@app.route("/books", methods=["GET"])
def list_books():
    books = library_use_cases.list_books()
    return jsonify([vars(book) for book in books])

@app.route("/books", methods=["POST"])
def add_book():
    data = request.json
    new_book = library_use_cases.add_book(data["title"], data["author"])
    return jsonify(vars(new_book)), 201

@app.route("/books/<int:book_id>/borrow", methods=["POST"])
def borrow_book(book_id):
    try:
        borrowed_book = library_use_cases.borrow_book(book_id)
        return jsonify(vars(borrowed_book))
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
