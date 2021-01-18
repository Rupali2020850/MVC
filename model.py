from random import randrange
import json

acc_start = 1000000000
acc_end = 10000000000

class Account:

    def __init__(self, acc_no, username, pin, balance=0):
        self.acc_no = acc_no
        self.username = username
        self.pin = pin
        self.balance = balance

    @classmethod
    def create_acc(cls, username, pin):
        acc_no = randrange(acc_start, acc_end)
        # json.load is used to convert a json file object to a python object
        with open("bank.json", "r+") as f:
            bank_dict = json.load(f)
        while acc_no in bank_dict:
            acc_no = randrange(acc_start, acc_end)

        acc = Account(acc_no, username, pin, 0)
        acc.save()
        return acc

    def save(self):
        with open("bank.json", "r+") as f:                          # a+ is the append mode
            bank_dict = json.load(f)
        bank_dict[self.acc_no] = {'username': self.username, 'pin': self.pin, "balance": self.balance}
        # print(bank_dict)
        with open("bank.json", "w+") as f:                          # w+ is the write mode
            json.dump(bank_dict, f, indent=4)
        return 

    @classmethod
    def login(cls, acc_no, pin):
        with open("bank.json", "r+") as f:
            bank_dict = json.load(f)
        
        if acc_no in bank_dict and bank_dict[acc_no]["pin"] == pin:
            # print("Credentials Matched.")
            username = bank_dict[acc_no]["username"]
            balance = bank_dict[acc_no]["balance"]
            acc = Account(acc_no, username, pin, balance)
            return acc
        else:
            # print("Incorrect Credentials.")
            return False


    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        self.save()
        return True

    def withdraw(self, withdrawal_amount):
        if withdrawal_amount <= self.balance:
            self.balance -= withdrawal_amount
            self.save()
            return True
        else:
            return False

    