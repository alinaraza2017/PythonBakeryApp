menu = {
    'r': 'Red Velvet Cookie',
    'dc': 'Dark Chocolate Cookie',
    'c': 'Caramel Cookie',
    'dcc': 'Double Chocolate Cookie',
}

prices = {
    'r': 180,
    'dc': 160,
    'c': 200,
    'dcc': 170,  # Assuming a price for Double Chocolate Cookie
}

cart = {}


def display():
    print("\nBiscuits:")
    for code, item in menu.items():
        print(f"{code}: {item} - Rs{prices[code]:.2f}")


def add_to_cart(item_code, quantity):
    if item_code in menu:
        if item_code in cart:
            cart[item_code] += quantity
        else:
            cart[item_code] = quantity
        print(f"{quantity} {menu[item_code]} added to the cart.")
    else:
        print("Invalid item code. Please choose from the menu.")


def display_cart():
    print("\nYour Cart:")
    for item_code, quantity in cart.items():
        print(f"{menu[item_code]}: {quantity}")
    total_amount = sum(prices[item_code] * quantity for item_code, quantity in cart.items())
    print(f"\nTotal Amount: Rs{total_amount:.2f}")


def main():
    display()

    while True:
        print("\nOptions:")
        print("1. Add item to cart")
        print("2. Display cart")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            item_code = input("Enter the code of your desired item: ").lower()
            if item_code in menu:
                try:
                    quantity = int(input("Enter the quantity: "))
                    if quantity > 0:
                        add_to_cart(item_code, quantity)
                    else:
                        print("Please enter a valid quantity (greater than 0).")
                except ValueError:
                    print("Invalid input. Please enter a valid quantity.")
            else:
                print("Invalid input, please choose from the menu.")

        elif choice == '2':
            display_cart()
        elif choice == '3':
            print("Thank you for visiting our bakery! Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

main()
