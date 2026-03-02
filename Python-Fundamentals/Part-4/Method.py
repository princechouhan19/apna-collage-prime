# Methods are functions defined inside a class that operate on instances of the class. They can be categorized into three types: instance methods, class methods, and static methods.

class Laptop:
    storage_type = "SSD"

    def __init__(self,Ram,Storage,brand,model):
        self.Ram = Ram
        self.Storage = Storage
        self.brand = brand
        self.model = model

    # Instance method to get laptop information
    def get_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, RAM: {self.Ram}, Storage: {self.Storage}, Storage Type: {Laptop.storage_type}"
    
    @classmethod 
    def get_storage_type(cls):
        print(f"Current storage type: {cls.storage_type}")

    @staticmethod
    def calc_discount(price,discount):
        final_price = price - ( discount * price / 100)
        print(f"Final price after discount: {final_price}")

l1 = Laptop("16GB","512GB","Dell","XPS 15")
l2 = Laptop("8GB","256GB","HP","Envy 13")

print("------- Instance Method ----------")

print(l1.get_info())
print(l2.get_info())

print("------- Class Method ----------")

Laptop.get_storage_type() # Calling class method on the class
print(l1.get_storage_type()) # Calling class method on an instance

print("------- Static Method ----------")

l1.calc_discount(4000,1000) # Calling static method on an instance