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
"""
def customer_transaction():
    while True:
        print(f"What would you like to do?\n")

        print("Enter 1 to deposit")
        print("Enter 2 to withdraw")
        print("Enter 3 to check balance\n")

        transaction = int(input("Enter option: "))

        if transaction == 1:
            print("\nHow much would you like to deposit?")
        elif transaction == 2:
            print("\nHow much would you like to withdraw?")
        elif transaction == 3:
            print("\nYour balance is ")
        else:
            print("Please enter a valid option\n")
        break
    
    amount = int(input("Amount($): "))


def main():
    """
    Run all the functions in the program
    """
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
