class Atm():
    def __init__(self,balance=0,pin=None):
        self.__balance=balance
        self._pin_ = pin
        self.menu()

    def menu(self):
        while True:
            print("1.create a pin \n 2.check balance \n 3.deposit amount \n 4.withdraw amount \n 5.exit ")
            choice = int(input("enter your choice : "))

            if choice == 1:
                self.create_pin()
            elif choice == 2:
                self.check_balance()
            elif choice == 3:
                self.deposit()
            elif choice == 4:
                self.withdraw()
            elif choice == 5:
                print("Thank you!!!")
                break
            else:
                print("Invalid input")

    def create_pin(self):
        self._pin = int(input("Create your PIN: "))
        print("PIN created successfully")
    
    def verify_pin(self):
        entered_pin = int(input("Enter PIN: "))
        if entered_pin == self._pin:
            return True
        else:
            print("Wrong PIN")
            return False
    
    def check_balance(self):
        if self.verify_pin():
            print("current balance :",self.__balance)
    def deposit(self):
        if self.verify_pin():
            amount = int(input("enter amount you want to deposit :"))
            self.__balance += amount
            print("Deposit sucessfully!!")

    def withdraw(self):
        if self.verify_pin():
            amount = int(input("enter amount you want to withdraw : "))
            self.__balance -= amount
            print("Withdraw sucessfully!!!")

atm =Atm(5000)