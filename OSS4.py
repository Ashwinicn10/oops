# multilevel inheritance

class product():
    def __init__(self,product_name,price):
        self.product_name=product_name
        self.price=price
    def display_product(self):
        print("Product Name:",self.product_name)
        print("Price:",self.price)
    
class electronic(product):
    def __init__(self,product_name,price,brand,warranty):
        super().__init__(product_name,price)
        self.brand=brand
        self.warranty=warranty
    def display_eleectronic_product(self):
        print("Electronic product brand:", self.brand)
        print("Electronic product warranty:", self.warranty)

class mobilephone(electronic):
    def __init__(self,product_name,price,brand,warranty,ram,storage):
        super().__init__(product_name,price,brand,warranty)
        self.ram=ram
        self.storage=storage
    def dispaly_mobiledetails(self):
        print("Mobile Phone's RAM:", self.ram)
        print("Mobile Phone's Storage:", self.storage)

phone=mobilephone("iphone15",55000,"Apple","1 year","16GB","128GB")
phone.display_product()
phone.display_eleectronic_product()
phone.dispaly_mobiledetails()