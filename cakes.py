menu = {
    'r': 'red velvet',
    'dc': 'dark chocolate',
    'c': 'caramel delight',
    'l': 'lemon tart',
}

prices = {
    'r': 1800,
    'dc': 1600,
    'c': 2000,
    'l': 1500,
}

cart={}

def display():
    print("\nCakes:")
    for item, flavor in menu.items():
        print(f"{item}: {flavor} - Rs{prices[item]:.2f}")


def add_to_cart(item, quantity):
    if item in menu:
        if item in cart:
            cart[item] += quantity
        else:
            cart[item] = quantity
        print(f"{quantity} {menu[item]} added to the cart.")
    else:
        print("Invalid item. Please choose from the menu.")

def display_cart():
    print("\nYour Cart:")
    for item, quantity in cart.items():
        print(f"{menu[item]}: {quantity}")
    total_amount = sum(prices[item] * quantity for item, quantity in cart.items())
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
            item = input("Enter the code of your desired flavor: ")
            if item in menu:
                quantity = int(input("Enter the quantity: "))
                add_to_cart(item, quantity)
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
