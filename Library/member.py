from user import User

class Member(User):
    def __init__(self,name,borrowed_items:list):
        super().__init__(name)
        self.borrowed_books:list = borrowed_items

    def borrow_books(self,book):
        if book.lend_book():
            self.borrowed_books.append(book)
            print(f'{self.name} has borrowed {book.title}')
        else:
            print(f'{book.title} is not available')

    def return_book(self,book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print(f'{self.name} returned the {book.title}')

        else:
            print(f'{book.title} does not exists with {self.name} user')


# m1 = Member('Kamlesh')
# print(m1.get_user_id(),m1.name)
#
# m2 = Member('Jaktap')
# print(m2.get_user_id(),m2.name)