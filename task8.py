# __contains__

class Library:
    def __init__(self, books):
        self.books = books

    def __contains__(self, item):
        return item in self.books


if __name__ == "__main__":
    library = Library(["Python", "Java", "C++", "Data Science"])

    print("Python" in library)      
    #print("Machine Learning" in library) 
