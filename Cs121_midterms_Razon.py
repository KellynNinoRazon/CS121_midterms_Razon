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
    Space()
    print("Game Library")
    for key, value in game_library.items():
        print(f"{key}:{value}")
    Message("Press enter to exit.")
    return
        
    
def Space():
    for i in range(3):
        print("")

def Message(message):
    input(message)
    Space()

def Inputs(max):
    try:
        inputs= int(input("What would you like to do?" ))
        Space()
        if inputs > max or inputs < 0:
            print("not available, choose a different option")
            input()
            return
        return inputs
        
    except ValueError:
            print("not available, choose a different option")
            input()
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
            user_accounts[username] = {"Username":username, "Password":password, "Budget" : 0,"Redeemable points":0,"Inventory":[]}
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
    display_available_games()

    rent=input("Check inventory?(y/n) ")
    if rent =="y":
        display_inventory(username)
    else:
        pass

    renting_game= input("Which game would you like to rent? ")
    game_cost=game_library[renting_game]["cost"]
    if renting_game in game_library:
        if game_library[renting_game]["quantity"]>0:
            user_accounts[username]["Inventory"].append(renting_game)
            if user_accounts[username]["Budget"]>game_cost:
            
                if renting_game in user_accounts[username]["Inventory"]:
                    print("Game Rented.")
               
                    game_points=game_cost/2
                    user_accounts[username]["Redeemable points"]+=game_points

                    user_accounts[username]["Budget"]-=game_cost

                    game_library[renting_game]["quantity"]-=1  
                    input()
                    return
                else:
                    print("Error, game cannot be rented")
                    return
            else:
                Message("You do not have enough budget. top-up first.")
                return
        else:
            print("Sorry no more copies available")
            return
    else:
        print("Sorry, Game does not exist in the Library")
        return
    
# Function to return a game
def return_game(username):
    display_inventory(username)
    returning_game=input("Which game to return? ")
    if returning_game in user_accounts[username]["Inventory"]:
        user_accounts[username]["Inventory"].remove(returning_game)
        Message("Thank you for returning the game")
    else:
        Message("No game found in your inventory")


# Function to top-up user account
def top_up_account(username, amount):
    try:
        amount=int(input("How much do you want to top-up:"))
        user_accounts[username]["Budget"]+=amount

        Message("Top-upped!")
        return
        
    except ValueError:
            print("Only type a numerical amount")
            input()
            return
    
# Function to display user's inventory
def display_inventory(username):
    print(user_accounts[username]["Inventory"])

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

# Function to handle user's logged-in menu
def logged_in_menu(username):
    while True:
        print("Welcome to the GameLib " + username)
        print("1.View Library\n2.Rent games\n3.Return game\n4.Top-up\n4.Check info")
    
        choice=Inputs(5)

        if choice==1:
            display_available_games()
        if choice==2:
            rent_game(username)
        if choice==3:
            return_game(username)
        if choice==4:
            top_up_account(username, user_accounts[username]["Budget"])
        if choice==5:
            check_credentials(username,user_accounts[username])  


# Function to check user credentials
def check_credentials(username, password):
    Space()
    print("Account info")
    for key, value in user_accounts[username].items():
        print(f"{key}:{value}")
    input()
    Space()
    return
  
# Main function to run the program
def main():
    while True:
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