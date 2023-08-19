import gspread
from google.oauth2.service_account import Credentials

"""
Connect spreadsheet to python to retrieve and update
customer details and transactions
"""
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('attempt_bank')


"""
A function to take details from customer and 
register the customer
"""
def register_customer():

    while True:
        try:

            customer_name = input("\nEnter your name: \n")
            if(not customer_name.isalpha()):
                print("Invalid. Please enter a valid name")
                continue

        except ValueError:
            print("Invalid. Please enter a valid name")
            
        break

    while True:
        try:

            customer_gender = input("\nEnter your gender(Male/Female/Others): \n")
            if(not customer_gender.isalpha()):
                print("Invalid. Please enter a valid gender")
                continue

            if customer_gender == "Male":
                print("I am Male")
            elif customer_gender == "Female":
                print("I am Female")
            elif customer_gender == "Others":
                print("I am Others")
            else:
                print("Enter a valid Gender")
                continue

        except ValueError:
            print("Invalid. ")
            continue
            
        break

    while True:
        try:

            customer_age = int(input("\nEnter your Age: \n"))

        except ValueError:
            print("Invalid. Please enter a valid age")
            continue

        if customer_age < 18:
            print("You must be 18years and above")
            continue
        break
    
    print(f"\nYou are welcome {customer_name}!")
    print(f"({customer_name}, {customer_gender}, {customer_age}years old)")

    return customer_name, customer_gender, customer_age
    

"""
This function allows a customer to make transactions
Checks the transaction selected by the user and
validates the input
"""
# Declaring a global list to hold customer intention so
# i can loop through them to determine the option a
# user selected and act base on the selection
entered_list = []

def customer_intention():
    while True:
        print(f"\nWhat would you like to do?\n")

        print("Enter 1 to Deposit")
        print("Enter 2 to Withdraw")
        print("Enter 3 to Check balance")
        print("Enter 4 to Exit\n")

        try:
            entered = int(input("Enter option: "))
            entered_list.append(entered)
            
            if entered == 1:
                print("\nHow much would you like to deposit? (Maximum of 50000)")
                break
            elif entered == 2:
                print("\nHow much would you like to withdraw? (Maximum of 50000)")
                break
            elif entered == 3:
                print("\nYour balance is ")
                break
            elif entered == 4:
                print("\nExit")
                break
            else:
                print(f"You entered '{entered}', Please enter a valid option (1 - 4)\n")     
                
        except ValueError:
            print(f"Invalid data, please try again.\n")


"""
Handles the deposits of customers
"""
def deposit():
    initial_balance = 0
    account_balance = 0

    while True:
        try:
            amount = int(input("Amount($): \n"))
            if amount > 50000:
                print(f"You entered {amount}, Maximum amount is 50000")
                continue
            break   

        except ValueError:
            print("Invalid amount. Try again")

    for enter in range(len(entered_list)):
        if entered_list[enter] == 1:

            updated_balance = initial_balance + amount
            account_balance += updated_balance

            print("\nUpdating your account balance...\n")
            print(f"Your account has been credited with the sum of: ${updated_balance}\n")
            print("Bye!\n")

            break

    return updated_balance


"""
Runs all the functions in the program
"""
def main():
    customer_details = register_customer()
    customer_intention()
    updated_balance = deposit()


"""
Prints a welcome message
"""
print("\n************************")
print("Welcome to ATTEMPT BANK")
print("************************\n")


"""
Call the main function to 
start running the program
"""
main()
