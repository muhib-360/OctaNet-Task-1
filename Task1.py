# Task 1 : ATM Machine Simulation

import random

class ATM:

    def __init__(self , user_name , bank_name , account_number ,phone_number, address, depos_count , withdr_count):

        self.user_name = user_name
        self.bank_name = bank_name
        self.account_number = account_number
        self.phone_number = phone_number
        self.address = address
        self.balance = 0
        self.PIN = self.generatePIN()
        self.menu = self.main()
        self.depos_count = 0
        self.withdr_count = 0


    def Menu(self):

        heading = (" | Welcome to ATM Machine | \n\n")
        print(heading.center(150))

        print(f"Hi {self.user_name}".center(150))

        print(" | Enter 1 for Show Details | ")
        print(" | Enter 2 for Cash Deposit | ")
        print(" | Enter 3 for Cash Withdraw | ")
        print(" | Enter 4 for Transaction History | ")
        print(" | Enter 5 for Balance Inquiry | ")
        print(" | Enter 6 for Changing PIN | ")
        print(" | Enter 0 for exit | \n")


    def main(self):
        while True:
            self.Menu()
        
            try:
                prompt = int(input("Enter the option : \n"))

            except ValueError:
                print("Invalid Input. Please enter a number")

                continue

            match prompt:
                case 0:
                    return
                case 1:
                    self.show_details()
                case 2:
                    self.deposit_cash()
                case 3:
                    self.withdraw_cash()
                case 4:
                    self.generate_history()
                case 5 :
                    self.balance_inquiry()
                case 6 :
                    self.change_PIN()
                case _:
                    print("Invalid Input !")


    def deposit_cash(self):
        self.depos_count = 0
        prompt = int(input(f" Hi {self.user_name}, Enter the amount you want to deposit : "))

        if prompt == 0:
            print("Invalid Amount !")
        self.balance+=prompt
        self.depos_count+=prompt
        print(f"Account Balance : {self.balance}")
        return self.balance

    def withdraw_cash(self):
        self.withdr_count = 0
        prompt = int(input(f"Hi {self.user_name} Enter the amount you want to withdraw : "))

        if prompt == 0:
            print("Invalid Input !")
            
        elif self.balance == 0:
            print("Zero Balance ! \n Recharge your Account")

        elif (prompt and self.balance) > 0: 
            self.balance = self.balance - prompt
            self.withdr_count+=prompt
            print(f"Account Balance : {self.balance}")
        return self.balance

    def generatePIN(self):
        self.pin = random.randrange(1000,9999)

    def change_PIN(self):
        self.old_PIN = self.pin

        self.new_pin = int(input("Enter the PIN : "))
        self.pin = self.new_pin

        print("Your PIN has been changed !")
        return self.pin
    
    def generate_history(self):
        print(" | ATM History | \n")
        print(f"User Name : {self.user_name}")
        print(f"Account No : {self.account_number} ")
        print(f"Cash Deposited : {self.depos_count}")
        print(f"Cash Withdrawed : {self.withdr_count}")
        print(f"PIN Changed from {self.old_PIN} ---> {self.pin}")

    def show_details(self):
        print(f"Bank Name : {self.bank_name}")
        print(f"Account Holder : {self.user_name}")
        print(f"Account Number : {self.account_number}")
        print(f"Address : {self.address}")
        print(f"Phone Number : {self.phone_number}")
        print(f"PIN Number : {self.pin}")

    def balance_inquiry(self):
        print(f"Balance : {self.balance}")
        return self.balance


User1 = ATM("Muhib Ali", "Meezan Bank Limited" , 95301133246 , 3352341354 , "C-156 Gulshan e Hadeed Phase 2 Extension Karachi" , depos_count=0, withdr_count=0)

User1.Menu()
# User1.show_details()
# User1.deposit_cash()
# User1.withdraw_cash()






    

    








    



