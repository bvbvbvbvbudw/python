class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def __repr__(self):
        return f"'{self.title}' by {self.author} ({self.year}), Genre: {self.genre}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"{book.title} added to library")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"'{title}' removed from library.")
                return
        print(f"'{title}' not found.")

    def find_books_by_author(self, author):
        result = []
        for book in self.books:
            if book.author == author:
                result.append(book)
        return result if result else f"books by {author} not found"

    def find_books_by_genre(self, genre):
        result = []
        for book in self.books:
            if book.genre == genre:
                result.append(book)
        return result if result else f"books in genre {genre} not found."

    def sort_books_by_year(self):
        return sorted(self.books, key=lambda book: book.year) # lambda - бо в key треба фнк, lambda це анонім фнк просто повератає book.year

    def sort_books_by_title(self):
        return sorted(self.books, key=lambda book: book.title)

    def display_books(self):
        if not self.books:
            print("library is empty.")
        else:
            for book in self.books:
                print(book)

library = Library()

library.add_book(Book("title1", "author1", 2021, "genre1"))
library.add_book(Book("title2", "author2", 2022, "genre2"))
library.add_book(Book("title3", "author3", 2023, "genre3"))

print("\nfind book 'author2':")
print(library.find_books_by_author("author2"))

print("\nfind book genre 'genre1':")
print(library.find_books_by_genre("genre1"))

print("\nbook sort year:")
for book in library.sort_books_by_year():
    print(book)

print("\nbook sort name:")
for book in library.sort_books_by_title():
    print(book)

library.remove_book("title3")

print("\nlist book after removing:")
library.display_books()
