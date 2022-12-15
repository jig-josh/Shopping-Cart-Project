class Customer:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.total = 0

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def show_customer_items(self):
        for item in self.items:
            return f"Name: {item.name}, Quantity: {item.quantity}, Price: {item.price} "

    def add_item_into_items(self, item):
        self.items.append(item)
        self.total += (float(item.price) * int(item.quantity))

    def get_items(self):
        return self.items

    def save_items_in_file(self, output_filename):
        with open(output_filename, 'w') as output_file:
            for item in self.items:
                subtotal = int(item.quantity) * float(item.price)
                output_file.write(" ".join([item.name, str(item.quantity),  str(subtotal)]))
                output_file.write("\n")
