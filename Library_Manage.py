
# Library Management System

class Library:
    
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        print(book, "Added successfully.")
        
    def issue_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(book, "Issued successfully.")
        else:
            print("Book not avaliable")
            
    def return_book(self, book):
        self.books.append(book)
        print(book, 'Returned successfully.')
        
    def show_books(self):
        if len(self.books) == 0:
            print("No book available.")
        else:
            print("\nAvaliable books:2")
            
            for book in self.books:
                print(book)
                
library = Library()

while True:
    print("\n----- Library Menu -----")
    print("1. Add book")
    print("2. Issue book")
    print("3. Return book")
    print("4. Show books")
    print("5. Exit")
    
    choice = int(input("Enter your choice:"))
    
    if choice == 1:
        book = input('Enter book name:')
        library.add_book(book)
        
    elif choice == 2:
        book = input("Enter book name to issue:")
        library.issue_book(book)
        
    elif choice == 3:
        book = input("Enter book name to return:")
        library.return_book(book)
        
    elif choice == 4:
        library.show_books()
        
    elif choice == 5:
        print("Thank you!")
        break
    
    else:
        print("Invalid choice!")