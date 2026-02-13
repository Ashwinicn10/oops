# __call__

class Calculator:
    def __call__(self, a, b):
        return a + b
if __name__ == "__main__":
    c = Calculator()
    print(c(10, 20))
