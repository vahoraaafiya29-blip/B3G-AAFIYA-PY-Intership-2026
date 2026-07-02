class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, title):
        self.__books.append(title)

    def remove_book(self, title):
        if title in self.__books:
            self.__books.remove(title)
            print(title,"Removed")

        else:
            print(title,"Not Found")      


    def list_books(self):
        print("Books in Library:")
        for book in self.__books:
         print(book)

library = Library()

library.add_book("Phython")
library.add_book("Java")
library.add_book("C++")

library.list_books()

library.remove_book("Java")

library.list_books()