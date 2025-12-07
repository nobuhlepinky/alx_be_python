

class Book:
    
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_details(self):
        
        return f"Book: {self.title} by {self.author}"



class EBook(Book):
    
    def __init__(self, title, author, file_size):
      
        super().__init__(title, author)
        self.file_size = file_size

    def get_details(self):
        
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"



class PrintBook(Book):
    
    def __init__(self, title, author, page_count):
        
        super().__init__(title, author)
        self.page_count = page_count

    def get_details(self):
       
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    
    def __init__(self):
        
        self.books = []

    def add_book(self, book):
       
        if isinstance(book, Book):
            self.books.append(book)
            print(f"Added: '{book.title}' to the library.")
        else:
            print("Error: Item is not a valid Book type.")

    def list_books(self):
       
        print("\n--- Current Library Collection ---")
        if not self.books:
            print("The library is empty.")
            return

    
        for book in self.books:
            print(book.get_details())