def startup_prompt():
    menu = """
    Welcome to the teller app!
    Please enter an option:
    1. Login
    2. Create Account
    3. Exit"""
    print(menu)
    choice = input()
    return choice


def login_prompt():
    acc_no = input("Please enter your account number: ")
    pin = input("Please enter your pin: ")
    return acc_no, pin

def get_pin():
    pin_1 = input("Please enter your pin: ")
    pin_2 = input("Please re-enter your pin: ")
    return pin_1, pin_2

def create_acc_prompt():
    username = input("Please enter your username: ")
    pin_1, pin_2 = get_pin()
    while pin_1 != pin_2:
        print("Pins did not match. Re-enter pin.")
        pin_1, pin_2 = get_pin()
    return username, pin_1

def incorrect_choice():
    print("Invalid option Selected.")
    return

def incorrect_creds():
    print("The credentials entered are incorrect.")
    return

def successful_login():
    print("Login Was Successful.")


def transaction_choice():
    menu = """
    Please enter your choice:
    1. Check Balance
    2. Deposit
    3. Withdraw
    4. Logout
    """
    print(menu)
    choice = input()
    return choice

def display_balance(acc):
    print(f"Hi {acc.username}! Your balance is INR {acc.balance}.")
    return

def get_deposit():
    deposit_amount = float(input("Please enter the amount that you would like to deposit."))
    return deposit_amount

def get_withdrwal():
    withdrawal_amount = float(input("Please enter the amount that you would like to withdraw."))
    return withdrawal_amount

