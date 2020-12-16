class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price


class Periodical(Publication):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher


class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)
        # self.title = title
        self.author = author
        self.pages = pages
        # self.price = price


class Magazine(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, period, publisher)
        # self.title = title
        # self.publisher = publisher
        # self.price = price
        # self.period = period


class Newspaper(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, period, publisher)
        # self.title = title
        # self.publisher = publisher
        # self.price = price
        # self.period = period


b1 = Book('Book1', 'Navjot', 311, 29.0)
m1 = Magazine('Mag1', 'Spring', 5.99, 'Monthly')
n1 = Newspaper('New1', 'Ny', 6.0, 'Daily')

print(b1.author)
print(m1.publisher)
print(n1.publisher)
