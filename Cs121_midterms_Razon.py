# Dictionary to store game library with their quantities and rental costs
game_library = {
    "Donkey Kong": {"quantity": 3, "cost": 2},
    "Super Mario Bros": {"quantity": 5, "cost": 3},
    "Tetris": {"quantity": 2, "cost": 1},
    # Add more games as needed
}

# Dictionary to store user accounts with their balances and points
user_accounts = {}
# Admin account details
admin_username = "admin"
admin_password = "adminpass"

# Function to display available games with their numbers and rental costs
def display_available_games():
    print(game_library)
    Message("")
    
def Space():
    for i in range(3):
        print("")

def Message(message):
    input(message)

def Inputs(max):
    try:
        inputs= int(input("What would you like to do?" ))
        if inputs > max or inputs < 0:
            print("not available, choose a different option")
            return
        return inputs
    except ValueError:
            print("not available, choose a different option")
            return


# Function to register a new user
def register_user():
    while True:
        username = input("Enter username: ")
        if username in user_accounts:
            print("Username already exists.")
            Message("Try again")
            Space()
            continue
        else:
            password = input("Enter password: ")
            user_accounts[username] = {"Username":username, "Password":password, "Budget" : 0}
            print("Account created!")
            Space()
            main()
            break

def Log_in():
    user = input("Username: ")
    if user in user_accounts:
        passcode = input("Password: ")
        if user_accounts[user]["Password"] == passcode:
            print("Logged in!")
            input()
            logged_in_menu(user)
        else:
            print("Incorrect Password. Try Again.")
            input()
            Space()
            main()
    else:
        print("User not found. Create an account")
        input()
        Space()
        main()

# Function to rent a game
def rent_game(username):
    pass

# Function to return a game
def return_game(username):
    pass

# Function to top-up user account
def top_up_account(username, amount):
    print("topping up account")

# Function to display user's inventory
def display_inventory(username):
    pass

# Function for admin to update game details
def admin_update_game(username):
    pass

# Function for admin login
def admin_login():
    while True:
        admin_name= input("Admin's username:")
        if admin_name != admin_username:
            print("Wrong username")
            Message("Try again")
            Space()
            continue
        else:
            admin_pass=input("Admin's password:")
            if admin_pass != admin_password:
                print("Wrong password.Try again")
                Message("Try again")
                Space()
            else:
                print("Logged in as an Admin.")
                break
                admin_menu()
                
# Admin menu
def admin_menu():
    print("Logging in...")

# Function for users to redeem points for a free game rental
def redeem_free_rental(username):
    pass

# Function to display game inventory
def display_game_inventory():
    pass

# Function to handle user's logged-in menu
def logged_in_menu(username):
    print("Welcome " + username)
    print("1.View Library\n2.Rent games\n3.Check balance\n4.Check info")
    choice=Inputs(4)

    if choice ==1:
        display_available_games()
    if choice==2:
        rent_game(username)
    if choice==3:
        top_up_account(username)
    if choice==4:
        check_credentials(username, password)


# Function to check user credentials
def check_credentials(username, password):
    pass
    
# Main function to run the program
def main():

    print("Welcome to the GameLib!")
    print("1.Register\n2.Log in\n3.Log in as Admin\n4.View Library")

    choice = Inputs(4)

    if choice==1:
        register_user()
    if choice==2:
        Log_in()
    if choice==3:
        admin_login()
    if choice==4:
        display_available_games()


'''if __name__ == "__main__":'''

main()