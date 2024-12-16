import os

class User:
    def init(self):
        self.menu()
    
    def menu(self):
        while True:
            choice = int(input("""Enter your choice
                            1. Register
                            2. Login
                            3. Exit"""))
            if choice == 1:
                self.register()
            elif choice == 2:
                self.login()
            elif choice == 3:
                print("You are exiting the program")
                break
            else:
                print("Invalid choice. Please enter a valid choice.")

    def register(self):
        self.username = input("Enter a username: ")
        self.password = input("Enter a password: ")
        
        if os.path.exists(f"{self.username}.txt"):
            print("Username already exists. Please choose a different username.")
            return

        # Create a new file for the user
        with open(f"{self.username}.txt", "w+") as file:
            file.write(f"{self.username},{self.password}\n")
            print("User registered successfully.")
            Expense.main(self)
    
    def login(self):
        self.username = input("Enter username: ")
        self.password = input("Enter password: ")

        # Check if the user file exists
        if os.path.exists(f"{self.username}.txt"):
            with open(f"{self.username}.txt", "r") as file:
                # Read the password from the user file
                lines = file.readlines()
                for line in lines:
                    stored_username, stored_password = line.strip().split(',')
                    if self.username == stored_username and self.password == stored_password:
                        print("Login successful!")
                        Expense.main(self)
                    else:
                        print("Invalid username or password. Please try again.")
        else:
            print("User not found. Please register.")

class Expense(User):  

    def init(self):
        super().init()  
        self.categories = {'food': 0, 'transportation': 0, 'housing': 0, 'utilities': 0, 'entertainment': 0}

    def main(self):
        while True:
            print('\nExpense Tracker Menu:')
            print('1. Add Expense')
            print('2. Show Expenses')
            print('3. Exit')

            choice = input('Enter your choice (1/2/3): ')

            if choice == '1':
                print("""choose 1 category from below
                         1. Food
                         2. Transportation
                         3. Housing
                         4. Utilities
                         5. Entertainment    """)
                category = input('Enter expense category: ').lower()
                amount = float(input('Enter expense amount: '))
                self.add_expense(category, amount)
            elif choice == '2':
                self.display_expenses()
            elif choice == '3':
                print('Exiting Expense Tracker.')
                self.display_expenses()  # Call display method before exiting
                break
            else:
                print('Invalid choice. Please enter 1, 2, or 3.')

    def add_expense(self, category, amount):
        self.categories = {'food': 0, 'transportation': 0, 'housing': 0, 'utilities': 0, 'entertainment': 0}
        if category in self.categories:
            self.categories[category] += amount
            print(f'Expense of ₹{amount} added to {category} category.')
            with open(f"{self.username}.txt", "a+") as file:  # Append mode to keep previous data
                file.write(f"{amount},{category}\n")
        else:
            print(f'Category {category} not found.')

    def display_expenses(self):
        if os.path.exists(f"{self.username}.txt"):
            print(f'\nDisplaying Expenses for {self.username}:')
            with open(f"{self.username}.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    amount, category = line.strip().split(',')
                    print(f'Category: {category.capitalize()}, Amount: ₹{amount}')
        else:
            print("No expenses found.")

expense1 = Expense()