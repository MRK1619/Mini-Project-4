class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books Present In This Library are: ")
        for book in self.books: 
            print(" *" + book)
    
    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You Have Been Issued {bookName}. Please Keep It Safe And Return It Within 30 Days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, This Book Is Either Not Available Or Has Already Been Issued To Someone Else. Please Wait Until The Book Is Available")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks For Returning This Book!")

class Student: 
    def requestBook(self):
        self.book = input("Enter The Name Of The Book You Want To Borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter The Name Of The Book You Want To return: ")
        return self.book
         

if __name__ == "__main__":
    ParthaLibrary = Library(["WINGS OF FIRE", "BELIEVE IN YOUR SELF", "PINOCCHIO", "LORDS OF THE RING"])
    student = Student()
    while(True):
        welcomeMsg = '''\n ====== Welcome to PARTHA,S Library ======
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library
        '''
        print(welcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            ParthaLibrary.displayAvailableBooks()
        elif a == 2:
            ParthaLibrary.borrowBook(student.requestBook())
        elif a == 3:
            ParthaLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Have A Great Day Ahead!")
            exit()
        else:
            print("Invalid Choice!")