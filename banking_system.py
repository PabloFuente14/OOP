class User():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def show_details(self):
        print("User details")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gemder:", self.gender)
        
        
class Bank(User):
    def __init__(self, name, age, gender, tipo_cuenta):
        super().__init__(name, age, gender)
        self.balance = 0
        self.tipo_cuenta = tipo_cuenta
        
    def deposit(self,amount):
        self.amount = amount
        self.balance =  self.balance + amount
        print("Accoun balance has been updated to: ", self.balance)
        print("The last amount that was depossited was: ", self.amount)
        
    def withdraw(self, amount_less):
        self.amount_less = amount_less
        if(self.amount_less > self.balance):
            print("The withdraw:", self.amount_less ," is bigger than the current balance", self.balance, "So the transaction can't be done")
        else:    
            self.balance = self.balance - self.amount_less
            print("The current balance of the account after the withdraw is: ", self.balance)
            
    def view_balance(self):
        self.show_details()
        print("Account balance has been updated: ", self.balance)
            
        



