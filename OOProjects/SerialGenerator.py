#Class SerialGeneratos must increase by 1 the number of the serie each time the methos generate() is called
#A start number has to be given to the instance, and the serie is starting from that number
#A custom way of setting a new start number in the middle of the serie has to be implemented, using the property decorator
#By an class attribute, the numbers a part from the start number has to be stored 

class SerialGenerator():
    _numbers = []
    def __init__(self,start_num):
        self.start_num = start_num
        self._actual_num = self.start_num
        self.__number_of_serie = 0
  #custom way of managing the start number in the middle of the serie      
    @property
    def actual_num(self):
        return self._actual_num
    
    @actual_num.setter
    def actual_num(self,new_value):
        if new_value < 0:
            raise ValueError("Number need to be positive")
        else:
            self._actual_num = new_value
            
 #generate method and           
    def generate(self):
        self._actual_num += 1
        self.__number_of_serie += 1
        self.add_number()
        return self._actual_num 
        
#reset the actual num to the start num
    def reset_number(self):
        self._actual_num = self.start_num
        return self._actual_num
    
#adding each unique number to the class attb _numbers
    def add_number(self):
        if self._actual_num not in SerialGenerator._numbers:
            SerialGenerator._numbers.append(self._actual_num)
        return SerialGenerator._numbers

    
    def __hash__(self):
        return hash(self.actual_num)
    
    def __repr__(self):
        return  f"<SerialGenerator start={self.start_num} current={self.actual_num}>"

#Getting the list of numbers
    @classmethod
    def get_numers_list(cls):
         return SerialGenerator._numbers