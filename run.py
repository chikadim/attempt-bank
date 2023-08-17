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
    customer_name = input("Enter your name: \n")
    customer_gender = input("\nEnter your gender (M/F/Others): \n")
    customer_age = input("\nEnter your age: \n")

    print(f"\nYou are welcome {customer_name}!")


"""
This function allows a customer to make transactions
Checks the transaction selected by the user and
validates the input
"""
# Declaring a global list to hold entries
entered_list = []

def customer_transaction():
    while True:
        print(f"What would you like to do?\n")

        print("Enter 1 to deposit")
        print("Enter 2 to withdraw")
        print("Enter 3 to check balance")
        print("Enter 4 to exit\n")

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
    
    amount = int(input("Amount($): \n"))
    new_balance = deposit(amount)

"""
Handles the deposits of customers
"""
def deposit(credited):

    initial_balance = 0

    for enter in range(len(entered_list)):
        if entered_list[enter] == 1:
            updated_balance = initial_balance + credited
            print(f"\nAccount balance has been updated : ${updated_balance}")

            initial_balance += updated_balance

            break

    
    

"""
Run all the functions in the program
"""
def main():
    register_customer()
    customer_transaction()


"""
Print a welcome message
"""
print("\n************************")
print("Welcome to ATTEMPT BANK")
print("************************\n")


"""
Call the main function to 
start running the program
"""
main()
