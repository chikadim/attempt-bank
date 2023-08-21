
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
    """
    This function collects details from a user,
    validates the inputs, handles errors and retun
    the entered details
    """
    while True:
        try:

            customer_name = input("Enter your name: \n")
            if (not customer_name.isalpha()):
                print("Invalid. Please enter a valid name")
                continue

        except ValueError:
            print("Invalid. Please enter a valid name")

        break

    while True:
        try:

            customer_gender = input("\nEnter your gender(Male/Female/Any):\n")
            if (not customer_gender.isalpha()):
                print("Invalid. Please enter a valid gender")
                continue

            if customer_gender == "Male":
                print("I am Male")
            elif customer_gender == "Female":
                print("I am Female")
            elif customer_gender == "Any":
                print("I am Any")
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
    print("You have a starting balance of $2000. Enjoy!")

    return customer_name, customer_gender, customer_age


# Declaring a list to hold customer intention so
# i can loop through them to determine the option a
# user selected and act base on the selection
entered_list = []


def customer_goal():
    """
    This function updates spreadsheet with
    customers details, offers transaction options and
    checks option selected by the user, validates
    the input and calls the neccessary functions
    """
    customer_details = register_customer()
    initial_deposit = 2000

    data_of_customers = ()
    all_data = data_of_customers + customer_details + (initial_deposit,)

    update_customers_worksheet(all_data)

    while True:
        print(f"\nWhat would you like to do?")

        print("Enter 1 to Deposit")
        print("Enter 2 to Withdraw")
        print("Enter 3 to Check balance")
        print("Enter 4 to Exit\n")

        try:
            entered = int(input("Enter option: \n"))
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
    Handles the deposits input of users
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
    """
    Processes the deposit transaction and updates
    the transactions worksheet with the new balance
    """
    initial_balance = 0
    withdrawal = 0

    get_information = SHEET.worksheet("customers").get_all_values()
    get_last_row = get_information[-1]  # using slice to get the last row
    get_initial_deposit = int(get_last_row.pop())

    updated_balance = initial_balance + deposit_amount

    balance_after_deposit = get_initial_deposit + updated_balance

    print("\nUpdating your account balance...\n")
    print(f"Your account has been credited with ${updated_balance}")
    print(f"Your new balance is ${balance_after_deposit}\n")

    print("Goodbye!\n")

    transaction_details = ()
    update_worksheet = transaction_details + (balance_after_deposit,)
    update_worksheet += (withdrawal,)

    update_transactions_worksheet(update_worksheet)


def update_transactions_worksheet(data):
    """
    This function gets customers details
    and transaction, then updates the
    google spreadsheet
    """
    worksheet = SHEET.worksheet("transactions")
    worksheet.append_row(data)


withdrawal_amount = 0


def withdrawal():
    """
    This function takes the withdrawals
    inputs and validates it
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
    """
    This processes the withdrawals
    and returns the balance
    """
    deposit = 0

    get_information = SHEET.worksheet("customers").get_all_values()
    get_last_row = get_information[-1]  # using slice to get the last row
    get_balance = int(get_last_row.pop())

    new_balance = get_balance - withdrawal_amount

    print("\nProcessing...\n")
    print(f"${withdrawal_amount} has been debited from your account")
    print(f"Your new balance is ${new_balance}\n")

    print("Goodbye!\n")

    transaction_details = ()
    update_worksheet = transaction_details + (deposit,)
    update_worksheet += (new_balance,)

    update_transactions_worksheet(update_worksheet)


def check_balance():
    get_information = SHEET.worksheet("customers").get_all_values()
    get_last_row = get_information[-1]  # using slice to get the last row
    get_balance = int(get_last_row.pop())

    return get_balance


def update_customers_worksheet(data):
    """
    This function gets customers details
    and transaction, then updates the
    google spreadsheet
    """
    worksheet = SHEET.worksheet("customers")
    worksheet.append_row(data)


def exit():
    """
    Calls the main function when
    a user selects the exit option
    """
    main()


def main():
    """
    Runs all the functions in the program
    """
    # Prints a welcome message
    print("\n************************")
    print("Welcome to ATTEMPT BANK")
    print("************************\n")
    customer_goal()


# starts running the program
main()
