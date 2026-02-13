# __iter__ and __next__

class Counter:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.end:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration

if __name__ == "__main__":
    counter = Counter(1, 5)

    for i in counter:
        print(i)

        