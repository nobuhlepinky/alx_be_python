class Book:
    def __init__(self, title, author):

        self.title = title
        self.author = author
        
        self._is_checked_out = False 

    def check_out(self):
        """Marks the book as checked out (unavailable)."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Returns the current availability status."""
        return not self._is_checked_out

    def __str__(self):
        """Returns a string representation of the book for easy printing."""
        return f"{self.title} by {self.author}"    
    



class Library:
    """
    Manages a collection of Book objects and handles library operations.
    """
    def __init__(self):
        self._books = [] 

    def add_book(self, book):
        """Adds a Book instance to the library collection."""
        if isinstance(book, Book):
            self._books.append(book)
        else:
            print("Error: Only Book objects can be added to the library.")

    def _find_book(self, title):
        """Helper method to find a book by title."""
        for book in self._books:
            if book.title.lower() == title.lower():
                return book
        return None

    def check_out_book(self, title):
        """Checks out a book by title, marking it as unavailable."""
        book = self._find_book(title)
        if book:
            if book.check_out():
                # print(f"Successfully checked out: {book.title}")
                return True
            else:
                # print(f"'{book.title}' is already checked out.")
                return False
        # print(f"Error: Book '{title}' not found in the library.")
        return False

    def return_book(self, title):
        """Returns a book by title, marking it as available."""
        book = self._find_book(title)
        if book:
            if book.return_book():
                # print(f"Successfully returned: {book.title}")
                return True
            else:
                # print(f"'{book.title}' was already available.")
                return False
        # print(f"Error: Book '{title}' not found in the library.")
        return False

    def list_available_books(self):
        """Prints the title and author of all books that are currently available."""
        available_found = False
        for book in self._books:
            if book.is_available():
                print(book)
                available_found = True
        
        if not available_found:
           
            # print("No books are currently available.")
            pass
