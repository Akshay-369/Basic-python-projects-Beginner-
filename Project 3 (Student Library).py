class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvaliableBooks(self):
        print('Books present in this Library are: ')
        for book in self.books:
            print(" > " + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f'You have issued {bookName}, Please keep it safe')
            self.books.remove(bookName)
            return True
        else:
            print('Sorry, This book is either not available or has been already issued by someone, Please wait untill the book is available')
            return False

    def returnBook (self, bookName):
        self.books.append(bookName)
        print('Thanks for returning the book! Hope you enjoyed reading it.')

class Student:
    def requestBook(self):
        self.book = input('Enter the name of the book you want to borrow: ')
        return self.book

    def returnBook(self):
        self.book = input('Enter the name of the book you want to return: ')
        return self.book


if __name__ == '__main__':
    centralLibrary = Library(['python', 'Django', 'Java', 'c++', 'Algorithms' ])
    student = Student()

    while(True):
        welcomeMsg = ''' \n -=-=-=-=- Welcome to Central Library -=-=-=-=-
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library
        '''
        print(welcomeMsg)
        a = int(input('Enter a choice: '))
        if a == 1:
            centralLibrary.displayAvaliableBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print('Thanks for choosing Central Library, Have a nice day')
            exit()
        else:
            print('Invalid Choice!')