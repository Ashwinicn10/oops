#__eq__

class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __eq__(self, other):
        if isinstance(other, Mobile):
            return self.brand == other.brand and self.model == other.model
        return False

if __name__ == "__main__":
    m1 = Mobile("Samsung", "S23", 80000)
    m2 = Mobile("Samsung", "S23", 85000)
    m3 = Mobile("Apple", "iPhone 15", 90000)

    print("m1 == m2:", m1 == m2)
    print("m1 == m3:", m1 == m3)

