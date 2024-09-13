class Customer:
    def __init__(self, name, new_bal):
        self.name = name
        if new_bal < 0:
           raise ValueError("Invalid balance!")
        self._balance = new_bal  #property attribute needs to be internal "_attname"
      
    @property #return the value of the attb
    def balance(self):
        return self._balance
       
    @balance.setter #set the value of the attb the way and comprobations wanted
    def balance(self, new_balance):
    
        if new_balance < 0:
            raise ValueError("Invalid balance!")
        else:
            self._balance = new_balance
        print("Setter method is called")
        

cust1 = Customer("Belinda", 2000)
cust1.balance= 3000
print(cust1.balance)