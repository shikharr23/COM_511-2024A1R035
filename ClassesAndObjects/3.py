"""
Create product class with the product name, price and quantity. Add an instance method to calculate the total cost.
Take these values from the user and display the product name and total cost.
"""


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_cost(self):
        return self.price * self.quantity

    def display(self):
        print(f"Name of product = {self.name} and total cost is {self.total_cost()}")



p1 = Product("Keyboard", 100, 10)
p1.display()

