import json
import os

BOOKS_FILE = "books.json"

def load_books():
    if not os.path.exists(BOOKS_FILE):
        return []
    with open(BOOKS_FILE, "r") as file:
        return json.load(file)

def save_books(books):
    with open(BOOKS_FILE, "w") as file:
        json.dump(books, file, indent=2)

def add_book(title, author):
    books = load_books()
    books.append({"title": title, "author": author, "read": False})
    save_books(books)
    print(f"Book '{title}' added.")

def remove_book(title):
    books = load_books()
    books = [book for book in books if book["title"].lower() != title.lower()]
    save_books(books)
    print(f"Book '{title}' removed.")

def list_books():
    books = load_books()
    if not books:
        print("No books found.")
        return
    for i, book in enumerate(books, 1):
        status = "Read" if book["read"] else "Unread"
        print(f"{i}. {book['title']} by {book['author']} - {status}")

def mark_as_read(title):
    books = load_books()
    for book in books:
        if book["title"].lower() == title.lower():
            book["read"] = True
            save_books(books)
            print(f"Marked '{title}' as read.")
            return
    print(f"Book '{title}' not found.")

def mark_as_unread(title):
    books = load_books()
    for book in books:
        if book["title"].lower() == title.lower():
            book["read"] = False
            save_books(books)
            print(f"Marked '{title}' as unread.")
            return
    print(f"Book '{title}' not found.")
