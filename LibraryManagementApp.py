# Creating class and giving it the name Library and two attributes, the library name and the list of books which will come as arguments when creating a Library object.
# The dictionary is not a parameter of Library since we're not passing it when creating the object, we are just initializing an emtpy dict.

class Library:
    def __init__(self,bookslist,name):
        self.booksList = bookslist
        self.name = name
        self.lendDict = {}

# Method to print out library name and available books
        
    def displayBooks(self):
        print(f'We have the following books in our library: {self.name}')
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
            print('Book added')

# Method to check if is book exists in booksList; if so, check if it is lended; if yes, print that out; if no, it can be lended and the lendDict be updated with key:value in the form of book:user

    def lendBook(self,book,user):
        if book in booksList:
            if book not in self.lendDict.keys():
                self.lendDict.update({book:user})
                print('Book has been lended. Database updated.')
            else:
                print(f'Book is already being used by {self.lendDict[book]}')
        else:
            print("Apologies, we don't have this book in our library")

# Method to check if a book is lended (exists in the lendDict) and remove it if so, completing the return. Otherwise, if the book does not exist in the lendDict, print that out

    def returnBook(self,book):
        if book in self.lendDict.keys():
            self.lendDict.pop(book)
            print('Book returned successfully')
        else:
            print('The book does not exist in the Book Lending Database')

# Method to display the menu and link the input options with the methods from the Library class
            
def main():
    while(True):
        print(f'Welcome to the {library.name} library. Following are the options,')
        choice = '''
                1. Display Books
                2. Lend a Book
                3. Add a Book
                4. Return a Book
                '''
        print(choice)

        userInput = input('Press Q to quit or C to continue:')
        if userInput == 'C':
            userChoice = int(input('Select an option to continue:'))
            if userChoice == 1:
                library.displayBooks()

            elif userChoice == 2:
                book = input('Enter the name of the book you want to lend:')
                user = input('Enter the name of the user:')
                library.lendBook(book,user)

            elif userChoice == 3:
                book = input('Enter the name of the book you want to add')
                library.addBook(book)

            elif userChoice == 4:
                book = input('Enter the name of the book you want to return:')
                library.returnBook(book)

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
    databaseName = input('Enter the name of the database file with extension:')
    bookDatabase = open(databaseName, 'r')
    for book in bookDatabase:
        booksList.append(book)
    library = Library(booksList,'PythonX')
    main()