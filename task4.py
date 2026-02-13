# Context Manager=__enter__ and __exit__

class DatabaseConnection:
    def __enter__(self):
        print("Database Connected")

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("Database Closed")

if __name__ == "__main__":
    with DatabaseConnection():
        print("Performing Query...")
