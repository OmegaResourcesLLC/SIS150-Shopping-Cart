# Name: Jeff Mendenhall
# Date: October 8, 2026
# Purpose: Create an online shopping cart program


class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0

    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print(
            f"{self.item_name} {self.item_quantity} "
            f"@ ${self.item_price:g} = ${total:g}"
        )


class ShoppingCart:
    def __init__(self, customer_name="none",
                 current_date="January 1, 2025"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        for index, item in enumerate(self.cart_items):
            if item.item_name == item_name:
                del self.cart_items[index]
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, updated_item):
        for item in self.cart_items:
            if item.item_name == updated_item.item_name:
                item.item_quantity = updated_item.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        return sum(
            item.item_price * item.item_quantity
            for item in self.cart_items
        )

    def print_total(self):
        print(
            f"{self.customer_name}'s Shopping Cart - "
            f"{self.current_date}"
        )
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
            print()
            return 0

        for item in self.cart_items:
            item.print_item_cost()

        print(f"Number of Items: {self.get_num_items_in_cart()}")

        total = self.get_cost_of_cart()
        print(f"Total: ${total:g}")
        return total


def print_menu():
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("o - Output shopping cart")
    print("q - Quit")


def execute_menu(menuOp, theCart):
    if menuOp == "a":
        print("ADD ITEM TO CART")
        item = ItemToPurchase()
        item.item_name = input("Enter the item name: ")
        item.item_price = float(input("Enter the item price: "))
        item.item_quantity = int(input("Enter the item quantity: "))
        print()

        theCart.add_item(item)

    elif menuOp == "r":
        print("REMOVE ITEM FROM CART")
        item_name = input("Enter name of item to remove:\n")
        theCart.remove_item(item_name)

    elif menuOp == "c":
        print("CHANGE ITEM QUANTITY")
        item = ItemToPurchase()
        item.item_name = input("Enter the item name:\n")
        item.item_quantity = int(input("Enter the new quantity:\n"))
        theCart.modify_item(item)

    elif menuOp == "o":
        print("OUTPUT SHOPPING CART")
        theCart.print_total()


if __name__ == "__main__":
    cust_name = input("Enter customer's name: ")
    day_date = input("Enter today's date: ")
    print()

    print(f"Customer name: {cust_name}")
    print(f"Today's date: {day_date}")

    my_cart = ShoppingCart(cust_name, day_date)

    print()
    print_menu()
    print()

    menu_choice = input("Choose an option:\n")

    while menu_choice != "q":
        if menu_choice in ["a", "r", "c", "o"]:
            execute_menu(menu_choice, my_cart)
            print_menu()
            print()

        menu_choice = input("Choose an option:\n")
