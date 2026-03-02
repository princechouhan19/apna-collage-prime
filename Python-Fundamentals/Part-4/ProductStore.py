# Design and create an online store for products . Track total products being created .  Create a ststic method to calculate discount on each product based on a % parameter . 

from itertools import count


class Product:
    count = 0

    def __init__(self , name , price):
        self.name = name
        self.price = price
        Product.count += 1
    
    def get_info(self):
        print(f"Price of {self.name} is {self.price}₹")

    @classmethod
    def get_count(cls):
        print(f"Total products created: {cls.count}")

    @staticmethod
    def calc_discount(price,discount):
        final_price = price - (discount * price /100)
        print(f"Final price after discount: {final_price}₹")
    
    
p1= Product("Laptop", 50000)
p2= Product("Smartphone", 20000)
p3= Product("Headphones", 5000)

print("------- Product Information ----------")
p1.get_info()
p2.get_info()
p3.get_info()

print("------- Discount Calculation ----------")
p1.calc_discount(p1.price,10) # 10% discount on Laptop
Product.calc_discount(p2.price,15) # 15% discount on Smartphone