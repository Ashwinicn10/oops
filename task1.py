#__str__ and __repr__

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"'{self.title}' by {self.author} - ₹{self.price}"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', price={self.price})"

if __name__ == "__main__":
    b1 = Book("Python Basics", "John Smith", 499)
    b2 = Book("Data Science Guide", "Alice Brown", 699)

    print(b1)

    print([b1, b2])

