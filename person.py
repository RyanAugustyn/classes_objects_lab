class Person:
    def __init__(self, name, money_amt):
        self.name = name
        self.money = money_amt
    
    #Method 1
    def remove_money(self, amount_to_withdraw):
        if self.money >= amount_to_withdraw:
            print(f"{amount_to_withdraw} dollars withdrawn from account")
            self.money -= amount_to_withdraw 
            print(f"You have {self.money} dollars remaining")
            return self.money
        else:
            print("Insufficient funds available!")
    #Method 2
    def add_money(self, amount_to_add, name_receiving_from):
        name = name_receiving_from 
        print(self.money)
        self.money = self.money + amount_to_add
        print(f"{name} has given you {amount_to_add} dollars")
        print(f"Your new total is {self.money}")