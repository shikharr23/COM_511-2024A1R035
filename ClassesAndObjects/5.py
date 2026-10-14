"""
Practice Problems
   1. Write a Python program that allows a librarian to add several books to a library.
   For each book, ask the user to enter its title and the number of copies. Store each book and its available copy count in a dictionary.

After the books have been added, display a menu that lets the user issue a book, return a book, display all books, or exit the program.
Apply these conditions:

* Book titles should be compared without distinguishing uppercase and lowercase letters.
* A book can be issued only if it exists in the library and at least one copy is available.
* Issuing a book decreases its available copy count by one.
* A book can be returned only if it exists in the library and at least one copy has already been issued.
* Returning a book increases its available copy count by one.
* Display an appropriate message for an unavailable book, an invalid choice, or an invalid number of copies.
"""

library = {}


num_of_books = int(input("Enter num of books: "))

for i in range(num_of_books):
    title = input("Enter book title: ").strip()
    copies = int(input("Enter num of copies: "))
    
    while copies <= 0:
        print("Invalid number")
        copies = int(input("Enter a valid number: "))
    
    library[title.lower()] = {
        "title" : title,
        "available" : copies,
        "issued" : 0
    }
    
while True:
    print("\n1.Issue a book")
    print("2. Return a book")
    print("3. Display all books")
    print("4. Exit")
    
    choice = input("Enter ur choice: ")
    
    if choice == "1":
        title = input("Enter book title: ").lower()
        
        if title not in library:
            print("Book not found")
        elif library[title]["available"] == 0:
            print("Book is not available")
        else:
            library[title]["available"] -= 1
            library[title]["issued"] += 1
            print("Book issued successfully")
    elif choice == "2":
        title = input("Enter the book title: ").lower()
        
        if title not in library:
            print("BOook not found")
        elif library[title]["issued"] == 0:
            print("No copy has been issued")
        else:
            library[title]["available"] += 1
            library[title]["issued"] -= 1
            print("Book returned successfully")
    elif choice == "3":
        if len(library) == 0:
            print("Library is empty")
        else:
            for book in library.values():
                print(book["title"])
    elif choice == "4":
        print("Exiting program")
        break
    else:
        print("Invalid choice")