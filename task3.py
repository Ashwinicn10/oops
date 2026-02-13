#__new__ & __init__

class User:
    def __new__(cls, name):
        print("Object is being created")
        return super(User, cls).__new__(cls)

    def __init__(self, name):
        self.name = name
        print("Object is initialized")

if __name__ == "__main__":
    u1 = User("Ashwini")



