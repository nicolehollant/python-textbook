import random

class Person:

    numActions = 10

    def __init__(self, name, pocketMoney=20):
        self.__name = name
        self.__salary = random.randint(100,500)
        self.__pocketMoney = pocketMoney
        self.__bankAccount = BankAccount(1250)
        self.__actions = 0
        print("Hi! I'm", self.__name)
    
    def work(self):
        print(self.__name, "went to work")
        if random.random() > .9:
            print("WOO!! I got a raise!!!")
            self.__salary *= 1.5
        self.__pocketMoney += self.__salary
        self.__actions+=1

    def gamble(self):
        print(self.__name, "hit the tables")
        r = random.random()
        if r > .999:
            print("We won big, baby!")
            self.__pocketMoney += 1000000
        elif r < .01:
            self.__pocketMoney *= -1
        else: 
            self.__pocketMoney -= self.__salary/2
        self.__actions+=1

    def deposit(self, amount):
        self.__bankAccount.deposit(amount)
        self.__pocketMoney -= amount
    
    def withdraw(self, amount):
        self.__bankAccount.withdraw(amount)
        self.__pocketMoney += amount

    def getName(self):
        return self.__name
    
    def getActions(self):
        return self.__actions

    def getBalance(self):
        return self.__bankAccount.getBalance()
    
    def getPocketMoney(self):
        return self.__pocketMoney

    def printPerson(self):
        print("Name:", self.__name)
        print("Salary:", self.__salary)
        print("Pocket Money:", self.__pocketMoney)
        print("Actions left:", str(Person.numActions - self.__actions))
        self.__bankAccount.printAccount()

class BankAccount:
   
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        self.__balance -= amount

    def getBalance(self):
        return self.__balance

    def printAccount(self):
        print("Bank balance:", self.__balance)

if __name__ == "__main__":
    print("Welcome to Hank's bank sim!")
    print("Work with 'j'")
    print("Gamble with 'g'")
    print("Print stats with 'p'")
    print("Deposit with 'd'")
    print("Withdraw with 'w'\n")
    hank = Person("Hank")
    while hank.getActions() < Person.numActions:
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
            print("Max deposit:", hank.getPocketMoney())
            amount = int(input("Deposit how much?\n >").strip().lower())
            if amount > hank.getPocketMoney(): 
                amount = hank.getPocketMoney()
            hank.deposit(amount)
        elif processed == "w":
            print("Max withdraw:", hank.getBalance())
            amount = int(input("Withdraw how much?\n >").strip().lower())
            if amount > hank.getBalance():
                amount = hank.getBalance()
            hank.withdraw(amount)
        else:
            try:
                # "hank._Person__bankAccount.deposit(100000)"
                eval(instruction)
            except Exception as e:
                print("Nice try, tough guy...")
    print("\nSIMULATION OVER")
    print(hank.getName(), "ending stats:")
    hank.printPerson()