import random

class Person:

    numActions = 10

    def __init__(self, name, pocketMoney=20):
        self.name = name
        self.salary = random.randint(100,500)
        self.pocketMoney = pocketMoney
        self.bankAccount = BankAccount(1250)
        self.actions = 0
        print("Hi! I'm", self.name)
    
    def work(self):
        print(self.name, "went to work")
        if random.random() > .9:
            print("WOO!! I got a raise!!!")
            self.salary *= 1.5
        self.pocketMoney += self.salary
        self.actions+=1

    def gamble(self):
        print(self.name, "hit the tables")
        r = random.random()
        if r > .999:
            print("We won big, baby!")
            self.pocketMoney += 1000000
        elif r < .01:
            self.pocketMoney *= -1
        else: 
            self.pocketMoney -= self.salary/2
        self.actions+=1

    def deposit(self, amount):
        self.bankAccount.deposit(amount)
        self.pocketMoney -= amount
    
    def withdraw(self, amount):
        self.bankAccount.withdraw(amount)
        self.pocketMoney += amount

    def printPerson(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Pocket Money:", self.pocketMoney)
        print("Actions left:", str(Person.numActions - self.actions))
        self.bankAccount.printAccount()

class BankAccount:
   
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount

    def getBalance(self):
        return self.balance

    def printAccount(self):
        print("Bank balance:", self.balance)

if __name__ == "__main__":
    print("Welcome to Hank's bank sim!")
    print("Work with 'j'")
    print("Gamble with 'g'")
    print("Print stats with 'p'")
    print("Deposit with 'd'")
    print("Withdraw with 'w'\n")
    hank = Person("Hank")
    while hank.actions < Person.numActions:
        hank.printPerson()
        instruction = input("\nWhat to do today?\n >")
        processed = instruction.strip().lower()
        if processed == "j":
            hank.work()
        elif processed == "g":
            hank.gamble()
        elif processed == "p":
            hank.printPerson()
        elif processed == "d":
            print("Max deposit:", hank.pocketMoney)
            amount = int(input("Deposit how much?\n >").strip().lower())
            if amount > hank.pocketMoney: 
                amount = hank.pocketMoney
            hank.deposit(amount)
        elif processed == "w":
            print("Max withdraw:", hank.bankAccount.balance)
            amount = int(input("Withdraw how much?\n >").strip().lower())
            if amount > hank.bankAccount.balance: 
                amount = hank.bankAccount.balance
            hank.withdraw(amount)
        else:
            try:
                # "hank.bankAccount.deposit(100000)"
                eval(instruction)
            except Exception as e:
                print("Nice try, tough guy...")
    print("\nSIMULATION OVER")
    print(hank.name, "ending stats:")
    hank.printPerson()