import model, view

def logon_loop():
    """3 options to the user:
    1. Login
    2. Create Account
    3. Exit"""
    choice = None
    while choice != '3':
        choice = view.startup_prompt()
        if choice=="1":
            acc_no, pin = view.login_prompt()
            acc = model.Account.login(acc_no, pin)
            while acc==False:
                view.incorrect_creds()
                acc_no, pin = view.login_prompt()
                acc = model.Account.login(acc_no, pin)
            view.successful_login()
            transaction_loop(acc)
        elif choice=="2":
            username, pin = view.create_acc_prompt()
            acc = model.Account.create_acc(username, pin)
            view.successful_login()
            transaction_loop(acc)
        elif choice=='3':
            return
        else:
            view.incorrect_choice()
            logon_loop()

def transaction_loop(acc):
    """Options:
    1. Check Balance
    2. Deposit
    3. Withdraw
    4. Logout"""
    choice = None
    while choice != "4":
        choice = view.transaction_choice()
        if choice == '1':
            view.display_balance(acc)

        elif choice == '2':
            deposit_amount = view.get_deposit()
            status = acc.deposit(deposit_amount)
            # if status == True:
                # view.successful_deposit() 
        elif choice == '3':
            withdrawal_amount = view.get_withdrwal()
            status = acc.withdraw(withdrawal_amount)
        elif choice == '4':
            return
        else:
            view.incorrect_choice()
            transaction_loop(acc)



if __name__ == "__main__":
    logon_loop()