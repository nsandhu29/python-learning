class Book:
    # Properties defined at class level are shared by all instance
    BOOK_TYPES = ('HARDCOVER', 'PAPERBACK', 'EBOOK')
    # double-underscore properties are hidden from other classes
    __booklist = None
    # create a class method works on class
    @classmethod
    def get_book_types(cls):
        return cls.BOOK_TYPES

    # Create a static method where we need to access properties of class
    # Singleton variable
    @staticmethod
    def get_book_list():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist
    # Instance function
    def __init__(self, new_title):
        self.title = new_title

    def __init__(self, title, book_type):
        self.title = title
        if (not book_type in Book.BOOK_TYPES):
            raise ValueError(f'{book_type} is not valid book type')
        else:
            self.book_type = book_type

# Access the class attributes
print("Book types", Book.get_book_types())

# Create instance of class
b1 = Book('Title1', 'HARDCOVER')
b2 = Book('Title2', 'PAPERBACK')

# Use static method to access a singleton object
the_books = Book.get_book_list()
the_books.append(b1)
the_books.append(b2)
print(the_books)