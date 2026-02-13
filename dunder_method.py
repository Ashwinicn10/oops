#Dunder methods (Double underscore methods) in Python are special methods that have double underscores at the beginning and end of their names. They are also known as magic methods or special methods.
#__new__
#__init__
#__len__
#__str__
#__repr__
#__add__
#__equal__
#__enter__
#__exit__

class Test:
    def __new__(cls):
        print("Object is being created")
        return super().__new__(cls)
    
    def __init__(self):
        print("Initialized object")

t=Test()