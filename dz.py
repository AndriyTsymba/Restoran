class FoodItem:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
class Menu:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)
    def remove_item(self, item):
        self.items.remove(item)
    def display_menu(self):
        for item in self.items:
            print(f"{item.name}: {item.description} - ${item.price}")
class Order:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)
    def remove_item(self, item):
        self.items.remove(item)
    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total
class Restaurant:
    def __init__(self):
        self.menu = Menu()
        self.orders = []
    def place_order(self, order):
        self.orders.append(order)
    def remove_order(self, order):
        self.orders.remove(order)
    def generate_bill(self, order):
        total = order.calculate_total()
        print("----- Bill -----")
        for item in order.items:
            print(f"{item.name}: ${item.price}")
        print("Total: $", total)
    def save_orders_to_file(self, filename):
        with open(filename, "w") as file:
            for order in self.orders:
                file.write("----- Order -----\n")
                for item in order.items:
                    file.write(f"{item.name}: ${item.price}\n")
                file.write(f"Total: ${order.calculate_total()}\n")
                file.write("\n")
pizza = FoodItem("Pizza Margarita","mozzarella cheese,fresh basil and olive", 10.99)
burger = FoodItem("Burger", "beef burger with tomato", 8.99)
pasta = FoodItem("Pasta", "spaghetti with tomato sauce", 5)
menu = Menu()
menu.add_item(pizza)
menu.add_item(burger)
menu.add_item(pasta)
print("Menu:")
menu.display_menu()
order = Order()
order.add_item(pizza)
order.add_item(burger)
restaurant = Restaurant()
restaurant.place_order(order)
restaurant.generate_bill(order)
restaurant.save_orders_to_file("orders.txt")