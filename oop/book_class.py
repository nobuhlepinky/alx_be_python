class Book:

    def __init__(self, title, author, year):
      
        self.title = title
        self.author = author
        self.year = year
        print(f"✅ Created Book: '{self.title}'")

    
    def __str__(self):
       
        return f"📖 {self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
     
        return f"Book('{self.title}', '{self.author}', {self.year})"

    
    def __del__(self):
      
        try:
            print(f"❌ Deleting {self.title}")
        except AttributeError:
            
            print(f"❌ Deleting an object...")



if __name__ == "__main__":
    print("\n--- Creating Objects (Calling __init__) ---")
    
    
    book1 = Book("1984", "George Orwell", 1949)
    
    
    book2 = Book("Brave New World", "Aldous Huxley", 1932)
    
    
    print("\n--- Testing __str__ (User Output via print()) ---")
    
    
    print("Printing book1:")
    print(book1)
    
    print("\n--- Testing __repr__ (Developer Output) ---")
    
    
    print("Official Representation of book2:")
    print(repr(book2)) 
    
    
    library = [book1, book2]
    print("\nLibrary contents (list uses __repr__):")
    print(library)
    
   
    print("\n--- Deleting Object Explicitly (Calling __del__) ---")
    
   
    del book1
    
    print("\n--- End of Script ---")
    