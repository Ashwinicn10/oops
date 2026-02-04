class book():
    def __init__(self, title, author):
        self.title=title
        self.author=author

    def display_book_details(self):
        print(f"Title: {self.title}, Author: {self.author}")

class issuedbook(book):
    def __init__(self, title, author, issued_to, issued_date):
        super().__init__(title, author)
        self.issued_to=issued_to
        self.issued_date=issued_date

    def display_issued_book_details(self):
        self.display_book_details()
        print(f"Issued to: {self.issued_to}, Issued date: {self.issued_date}")

issued_book = issuedbook("1984", "George Orwell", "John Doe", "2023-01-01")
issued_book.display_issued_book_details()