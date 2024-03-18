# Creating class and giving it the name Library and two attributes, the library name and the list of books which will come as arguments when creating a Library object.
# The dictionary is not a parameter of Library since we're not passing it when creating the object, we are just initializing an emtpy dict.

class Library:
    def __init__(self,bookslist,name):
        self.booksList = bookslist
        self.name = name
        self.lendDict = {}

        # First challenge requires a database for lended books. I imported it in __main__ and handled it in lendBook and returnBook methods; here, we are actually importing it's key-value pairs in our lendDict
        with open(lendedDatabase, 'r') as file:
            for line in file:
                book, user = line.split(':', 1)
                self.lendDict[book] = user
                
# Method to print out library name and available books
        
    def displayBooks(self):
        print(f"\nWe have the following books in our library: {self.name}")
        for book in self.booksList:
            print(book)

# Method to check if a book exists in booksList, otherwise add it to it and to the database file

    def addBook(self,book):
        if book in booksList:
            print('Book already exists')
        else:
            self.booksList.append(book)
            bookDatabase = open(databaseName, 'a')
            bookDatabase.write('\n')
            bookDatabase.write(book)
            bookDatabase.close() # added close for efficiency
            print('Book added')

# Method to check if is book exists in booksList; if so, check if it is lended; if yes, print that out; if no, it can be lended and the lendDict be updated with key:value in the form of book:user

    def lendBook(self,book,user):
        if book in booksList:
            if book not in self.lendDict.keys():
                self.lendDict.update({book:user})
                # First challenge from PythonX was to also create a database for lended books (asking for file path in __main__ as with book database)
                with open(lendedDatabase, 'a') as f:
                    f.write(f"{book}:{user}\n")
                with open(permanentLendedDatabase, 'a') as f: # First challenge ambigous, making sure we store current lenders in lendedDatabase and keeping a permanent record
                    f.write(f"{book}:{user}\n")
                print('Book has been lended. Database updated.')
            else:
                print(f'Book is already being used by {self.lendDict[book]}')
        else:
            print("Apologies, we don't have this book in our library")

# Method to check if a book is lended (exists in the lendDict) and remove it if so, completing the return. Otherwise, if the book does not exist in the lendDict, print that out

    def returnBook(self,book):
        if book in self.lendDict.keys():
            self.lendDict.pop(book)
            # Since First challenge requires a database for lended books, we must also have a way of deleting them when returned
            with open(lendedDatabase, 'r+') as f:
                    lines = f.readlines() # Reads each line and stores the content of it in a list
                    f.seek(0) # After getting to the end of the file, moves back the pointer to the beginning
                    for line in lines: # Check each element in the lines list
                        if book not in line: # If book not in line, writes back the line from lines to the file
                            f.write(line)
                    f.truncate() # Removes any extra whitespace or incorrect content
            print('Book returned successfully')
        else:
            print('The book does not exist in the Book Lending Database')

    # Second challenge from PythonX was to add a method that will return the record of the books that have been borrowed with the name of the person who has borrowed the book
    def currentlyLended(self):
        if not self.lendDict: # if Dict is empty
            print("\nNo current lenders\n")
        else:
            for book, user in self.lendDict.items():
                print(f'{book} is currently borrowed by {user}')

    # For second challenge, just to cover all time record as well
    def allTimeLended(self):
        with open(permanentLendedDatabase, 'r+') as f:
            lines = f.readlines() # Reads each line and stores the content of it in a list
            for line in lines: # Check each element in the lines list
                print(line)

    # Third challenge from PythonX was to have a remove method as well. This method removes the book first from the database and then from the booksList. Returning is still possible after removal.
    def removeBook(self,book):
        if book in booksList:
            with open(databaseName, 'r+') as f:
                lines = f.readlines() # Reads each line and stores the content of it in a list
                f.seek(0) # After getting to the end of the file, moves back the pointer to the beginning
                for line in lines: # Check each element in the lines list
                    if book not in line: # If book not in line, writes back the line from lines to the file
                        f.write(line)
                f.truncate() # Removes any extra whitespace or incorrect content
            booksList.remove(book)
        else:
            print("Book is not part of our library.")

            
# Method to display the menu and link the input options with the methods from the Library class
            
def main():
    while(True):
        print(f'\nWelcome to the {library.name} library. Following are the options,')
        choice = '''
                1. Display Books
                2. Lend a Book
                3. Add a Book
                4. Return a Book
                5. List current lenders
                6. List all time record
                7. Remove book
                '''
        print(choice)

        userInput = input('Press Q to quit or C to continue: ')
        if userInput == 'C':
            userChoice = int(input('Select an option to continue: '))
            if userChoice == 1:
                library.displayBooks()

            elif userChoice == 2:
                book = input('Enter the name of the book you want to lend: ')
                user = input('Enter the name of the user: ')
                library.lendBook(book,user)

            elif userChoice == 3:
                book = input('Enter the name of the book you want to add: ')
                library.addBook(book)

            elif userChoice == 4:
                book = input('Enter the name of the book you want to return: ')
                library.returnBook(book)

            elif userChoice == 5:
                library.currentlyLended()

            elif userChoice == 6:
                library.allTimeLended()

            elif userChoice == 7:
                book = input('Enter the name of the book to remove: ')
                library.removeBook(book)

            else:
                print('Please choose a valid option')
        elif userInput == 'Q':
            break
        else:
            print('Please enter a valid option')

# Main method like other programming languages as C, C++, etc. Instructs the interpreter to start code execution from here. __name__ is by default == '__main__'
# Created the bookList variable to pass into the Library class and name parameter is passed when creating the object
# Linking with database file and updating bookList with info from it
# Executing main() method

if __name__ == '__main__':
    booksList = []
    databaseName = input('Enter the name of the book database file with extension: ')
    lendedDatabase = input('Enter the name of the lended book database file with extension: ')
    permanentLendedDatabase = input('Enter the name of the permanent lended book database file with extension: ')
    bookDatabase = open(databaseName, 'r')
    for book in bookDatabase:
        booksList.append(book.strip()) # added strip otherwise the names of books would contain newline character and app wouldn't work appropriately 
    bookDatabase.close() # added close for efficiency
    library = Library(booksList,'PythonX')
    main()