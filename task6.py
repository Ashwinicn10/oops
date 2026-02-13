# __getitem__, __setitem__

class ShoppingCart:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

if __name__ == "__main__":
    cart = ShoppingCart(["Laptop", "Mouse", "Keyboard"])

    print("Item at index 0:", cart[0])

    cart[1] = "Headphones"

    print("Updated cart:", cart.items)