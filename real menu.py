a='Bakery Menu:'
print(a)

class EliteBakersMenu:
    def __init__(self):
        self.menu_options = {
            1: "Cakes",
            2: "Biscuit",
            3: "Bread",
            4: "Exit"
        }

    def display_menu(self):
        print("Welcome to the Home of ELITE taste!")
        for option, item in self.menu_options.items():
            print(f"{option}. {item}")

    def process_choice(self, choice):
        if choice == 4:
            print("Thank you for visiting Elite Bakers. Goodbye!")
            exit()
        elif choice in self.menu_options:
            print(f"You selected: {self.menu_options[choice]}")
            # Add your logic for each menu item here (e.g., order processing, delivery, etc.)
        else:
            print("Invalid choice. Please select a valid option.")

    def run(self):
        while True:
            self.display_menu()
            try:
                choice = int(input("Enter the number of your choice: "))
                self.process_choice(choice)
                if choice==1:
                    import os
                    os.system("cakes.py")
                
                if choice==2:
                    import os
                    os.system("biscuits.py")

                if choice=='1':
                    import os
                    os.system("breads.py")
            except ValueError:
                print("Invalid input. Please enter a number.")

             

if __name__ == "__main__":
    Elite_menu = EliteBakersMenu()
    Elite_menu.run()
