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
A function to to take details from customer and 
register the customer
"""
def register_customer():
    customer_name = input("Enter your name: \n")
    customer_gender = input("Enter your gender (M/F/Others): \n")
    customer_age = input("Enter your age: \n")

    print(f"\nYou are welcome {customer_name}!")




def main():
    """
    Run all the functions in the program
    """
    register_customer()


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
