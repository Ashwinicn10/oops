# def login(login_page):
#     def wrapper(user,password):
#         if user=="admin" and password=="1234":
#             print("Login successful")
#             login_page(user,password)
#         else:
#             print("Login failed")
#     return wrapper

# @login
# def login_page(user,password):
#     print("welcome to the dashboard")

# login_page("admin","1234")



# Decorator
def admin_only(func):
    def wrapper(username):
        if username == "admin":
            func(username)
        else:
            print("Access Denied")
    return wrapper

@admin_only
def dashboard(username):
    print("Welcome to Admin Dashboard")

dashboard("admin")
# dashboard("user123")  
