# __del__

class Session:
    def __init__(self):
        print("Session Started")

    def __del__(self):
        print("Session Ended")

if __name__ == "__main__":
    obj = Session()
    del obj           
