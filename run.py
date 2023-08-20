
import gspread
from google.oauth2.service_account import Credentials


# Connect spreadsheet to python to retrieve and update
# customer details and transactions
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('attempt_bank')


def register_customer():

    #print(f"\nYou are welcome {customer_name}!")
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
    print(f"({customer_name}, {customer_gender}, {customer_age}years old)\n")
    print(f"You have a starting balance of 2000. Enjoy!\n")



    return customer_name, customer_gender, customer_age


# Declaring a list to hold customer intention so
# i can loop through them to determine the option a
# user selected and act base on the selection
entered_list = []


def customer_intention():
    """
    This function allows a customer to make transactions
    Checks the transaction selected by the user and
    validates the input
    """
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
                print("\nHow much would you like to deposit?(Max of 2000)")
                deposit()
                process_deposit()
                break
            elif entered == 2:
                print("\nHow much would you like to withdraw?(Max of 2000)")
                withdrawal()
                process_withdrawal()
                break
            elif entered == 3:
                customer_balance = check_balance()
                print(f"\nYour balance is {customer_balance}")
                print("Thank you")
                break
            elif entered == 4:
                print("\nExit")
                exit()
                print(f"restarting...")
                break
            else:
                print(f"You entered '{entered}', Please option are (1 - 4)\n")
        except ValueError:
            print(f"Invalid data, please try again.\n")
            


deposit_amount = 0


def deposit():
    """
    Handles the deposits of customers
    """
    global deposit_amount
    while True:
        try:
            deposit_amount = int(input("Amount($): \n"))
            if deposit_amount > 2000:
                print(f"\nYou entered {deposit_amount}, Deposit limit is 2000")
                continue
            break
        except ValueError:
            print("Invalid amount. Try again")


def process_deposit():
    initial_balance = 0
    
    get_information = SHEET.worksheet("information").get_all_values()
    get_last_row = get_information[-1]  # using slice to get the last row
    get_balance = int(get_last_row.pop())

    updated_balance = initial_balance + deposit_amount
    
    balance_after_deposit = updated_balance + get_balance

    print("\nUpdating your account balance...\n")
    print(f"Your account has been credited with ${deposit_amount}\n")
    print(f"Your new balance is ${balance_after_deposit}\n")

    print("Goodbye!\n")


withdrawal_amount = 0


def withdrawal():
    """
    This function handles withdrawals
    """
    global withdrawal_amount
    while True:
        try:
            withdrawal_amount = int(input("Amount($): \n"))
            if withdrawal_amount > 2000:
                print(f"\nWithdraw limit is 2000")
                continue
            break

        except ValueError:
            print("Invalid amount. Try again")


def process_withdrawal():

    get_information = SHEET.worksheet("information").get_all_values()
    get_last_row = get_information[-1]  # using slice to get the last row
    get_balance = int(get_last_row.pop())

    new_balance = get_balance - withdrawal_amount

    print("\nProcessing...\n")
    print(f"${withdrawal_amount} has been debited from your account\n")
    print(f"Your new balance is ${new_balance}\n")

    print("Goodbye!\n")



def check_balance():
    get_information = SHEET.worksheet("information").get_all_values()
    get_last_row = get_information[-1]  # using slice to get the last row
    get_balance = int(get_last_row.pop())

    return get_balance


def update_worksheet(data):
    """
    This function gets customers details
    and transaction, then updates the
    google spreadsheet
    """
    information_worksheet = SHEET.worksheet("information")
    information_worksheet.append_row(data)


def exit():
    main()


def main():
    """
    Runs all the functions in the program
    """
    # Prints a welcome message
    print("\n************************")
    print("Welcome to ATTEMPT BANK")
    print("************************/n")
    print("You have $2000 as your balance. Thank you!")
    customer_details = register_customer()
    customer_intention()

    initial_deposit = 2000
    initial_balance = 2000

    data_for_spreadsheet = ()
    all_data = data_for_spreadsheet + customer_details + (initial_deposit,) + (withdrawal_amount,) + (initial_balance,)

    update_worksheet(all_data)
    

# starts running the program
main()

