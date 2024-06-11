all_books = {1001:'harry potter',1002:'lord of the ring'}
class Book(dict):
    def __init__(self):
       self.book_list = all_books
       self.issued_books={}
        
    def add_book(self,bid): 
        book_name=str(input('Enter book name : '))
        all_books[bid] = book_name  
        print(f'book {book_name} added to your library👍 \ncontinue....')
    
    def view_book(self):
        print('🏠/view book')
        print('-------------')
        try:
          bid = int(input('Enter book id to view book : '))
        except TypeError:
            print('please try to enter integer value')
            while type(bid) != int:
                bid = int(input('enter book id : '))
                if bid == int:
                    break
        if bid in self.book_list.keys():
            print(bid, self.book_list[bid])
        else:
            print("book id missmatch....😒")

class Library(Book):
    def __init__(self):
        super().__init__()

    def delete_book(self):
        print('🏠/Delete book')
        print('----------')
        try:
           key = int(input('Enter book id : '))
        except TypeError:
           print('please try to enter integer value')
           while type(key) != int:
                key = int(input('enter book id : '))
                if key == int:
                    break
        if key in self.book_list.keys():
            print()
            print(f"{self.book_list[key]} - Deleted from the library.")
            del self.book_list[key]
        else:
            print("Book id not found in the library.")

    def view_book_in_stock(self):
        print('🏠/Books in stock')
        print('--------------')
        print('|BOOK ID |    BOOK NAME ')
        print('|------- |    ---------')
        for key,value in self.book_list.items():
            print(f'|{key}    |    {value}')
        print('--------------------')

    def issue_book(self):
        print('🏠/Issue book')
        print('-----------')
        key = inputs()
        if key in self.book_list.keys():
            print()
            print(f"Book {self.book_list[key].upper()} - issued from the library.")
            value = self.book_list[key]
            self.issued_books[key] = value
        else:
            print("Book id not found in the library.")
        del self.book_list[key]
        
    def issued_books_list(self):
        print()
        print('🏠/Issued books list')
        print('------------------')
        print('|BOOK ID |    BOOK NAME ')
        print('|------- |    ---------')
        for key,value in self.issued_books.items():
            print(f'|{key}    |    {value}')
        print('--------------------')

    def return_book(self):
        print('🏠/Return book')
        print('------------')
        bid = inputs()
        if bid in self.issued_books.keys():
            value = self.issued_books[bid]
            self.book_list[bid] = value
        else:
            print('book id not found')

    def all_book(self):
        print()
        print('🏠/Books in our library')
        print('--------------------')
        print('|BOOK ID |    BOOK NAME ')
        print('|------- |    ---------')
        for key,value in all_books.items():
            print(f'|{key}    |    {value}')
        print('--------------------')

book1 = Book()
library1 = Library()

def inputs():
    try:
        bid = int(input('Enter 4 digit book id : '))
    except TypeError:
        print('please enter integer value')
        while type(bid) != int:
            bid = int(input('enter 4 book id : '))
            if bid == int:
                break 
    return bid

while True:  
     print()
     print('🏠')
     print('choose the following')
     print('---------------------')
     print('| 1.Add book \n| 2.Delete book \n| 3.View book \n| 4.Issue book \n| 5.View issued books \n| 6.Return book \n| 7.view all books \n| 8.quit')
     print('---------------------')
     try:
        option = int(input('enter the option number : '))
     except TypeError:
        print('wrong option')
        while type(option) != int:
            option = int(input('enter the option number : '))
            if option == int:
                break
     if option == 1:
        print()
        print('🏠/Add book')
        print('---------------')
        val = inputs()
        if (len(str(val)) != 4):
            print(f'You entered a {len(str(val))} digit value, enter 4 digit value😊')
            while len(str(val)) != 4:
                val = inputs()
                if len(str(val)) == 4:
                   break
                else:
                    print(f'You entered a {len(str(val))} digit value, enter 4 digit value😊')
        if len(str(val)) == 4 and val in all_books.keys():
            print(f'{val} already exist, try new one....')
            while len(str(val)) == 4 and val in all_books.keys():
                val = inputs()
                if len(str(val)) == 4 and val not in all_books.keys():
                   bid = val
                   book1 = Book()
                   book1.add_book(bid)
                   break
                else:
                    print(f'{val} already exist, try new one')
        else:
            bid = val
            book1.add_book(bid)
     elif option == 2:
       library1.delete_book()
     elif option == 3:
       book1.view_book()
     elif option == 4:
        library1.issue_book()
     elif option ==5:
         library1.issued_books_list()
     elif option == 6:
        library1.return_book()
     elif option == 7:
        library1.all_book()
     elif option == 8:
        break
     else:
         print()
         print('wrong option, try again')
