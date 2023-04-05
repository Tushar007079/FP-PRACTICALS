class BankAccount:
    def __init__(self, name, acc_type, balance):
        self.name = name
        self.acc_type = 'Current' if acc_type == 0 else 'Saving'
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} Depostied Succesfully.")
        else:
            raise ValueError(
                f"ERROR : Invalid Amount , Try Again! [Amount:{amount}]")
        print(f"Your Balance : {self.balance}\n")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"{amount} Withdrawn Succesfully.")
        print(f"Your Balance : {self.balance}\n")

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, bal):
        if bal >= 1000:
            self._balance = bal
        else:
            raise ValueError(f"ERROR : Minimum Balance must be 1000!")

    def show_details(self):
        print(f"{self.name}'s Account Details : ")
        print(f"Account Name : {self.name}")
        print(f"Account Type : {self.acc_type}")
        print(f"Account Balance : {self.balance}")


try:
    acc = BankAccount("James Bond", 1, 1000)
    while True:
        print("<1> Account Details")
        print("<2> Deposit")
        print("<3> Withdraw\n")

        choice = int(input("Enter Option : "))
        if choice == 1:
            acc.show_details()
        elif choice == 2:
            amt = int(input("Enter Amount : "))
            acc.deposit(amt)
        elif choice == 3:
            amt = int(input("Enter Amount : "))
            acc.withdraw(amt)
except Exception as e:
    print(e)
