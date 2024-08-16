from library_item import LibraryItem

class Book(LibraryItem):
    def __init__(self,title,author,isbn,available = True):
        # creating a book thats why providing the available value as True
        super().__init__(title, available)
        self.__author = author
        self._isbn = isbn

    # method overriding
    def lend_item(self):
        if self.is_available():
            self._mark_as_unavailable()
            print(f'{self._title} book has been lent out .')

        else:
            print(f'{self._title} book is not available for lending ')


    def return_item(self):
        self._mark_as_available()
        print(f'{self._title} book has been returned ')


    def give_author(self):
        return self.__author