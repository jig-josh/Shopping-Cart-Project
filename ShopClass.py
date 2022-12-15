from ItemClass import Item
from datetime import timedelta,datetime
import pandas as pd


class Shop:
    def __init__(self):
        self.tax_amount = 0.13
        self.available_items = []

    def add_available_items_from_file(self, input_filename):
        with open(input_filename, 'r') as input_file:
            file_items = input_file.readlines()

        for row in file_items:
            item = row.split()
            name = item[0]
            quantity = int(item[1])
            price = item[2]

            self.available_items.append(Item(name, quantity, price))

    def show_available_items(self):
        for item in self.available_items:
            print(f"Name: {item.name}, Quantity: {item.quantity}, Price: {item.price} ")
    
    def show_items_in_table(self):
                
        with open("available_grocery_items.txt", "r") as dr:
            dr.seek(0)
            df = pd.read_csv("available_grocery_items.txt", sep = " ", header=None, names = ["Items", "Quantity", "Price"])
            print("*****************************************")
            print(df)
            print("*****************************************")
            file_line = dr.readline()
            available_grocery_items = dr.readlines()
            dr.close()
    
    def sell_items(self, item_name, quantity, customer):
        for item in self.available_items:
            if item.name == item_name:
                if item.quantity > quantity:
                    item.quantity -= quantity
                    new_customer_item = Item(item.name, quantity, item.price)
                    customer.add_item_into_items(new_customer_item)
                    break
                else:
                    raise ValueError

    def save_items_in_file(self, output_filename):
        with open(output_filename, 'w') as output_file:
            for item in self.available_items:
                output_file.write(" ".join([item.name, str(item.quantity), str(item.price)]))
                output_file.write("\n")

    def get_order_pickup_time(self, datetime):
            return datetime 
            

    def show_welcome_message(self, customer):
        welcome_message = ("Welcome to my store " + customer.get_name().title() + ".")
        lenWCMsg = len(welcome_message)
        print("*" * lenWCMsg)
        print(welcome_message)
        print("*" * lenWCMsg)

    
