class BetterDate:    
    # Constructor
    def __init__(self, year, month, day):
      #  multiple variable assignments in one line
      self.year, self.month, self.day = year, month, day
    
    # class method from_str
    @classmethod
    def from_str(cls, datestr):
        # Split the string at "-" and convert each part to integer
        parts = datestr.split("-")
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        # Return the class instance
        return cls(year, month, day)
        
bd = BetterDate.from_str('2020-04-30')  
bd1 = BetterDate(2020, 4, 30) 
print(f"{bd.year} and {bd1.year} have same value but are created differently")
