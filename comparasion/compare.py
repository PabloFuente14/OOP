class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __eq__(self,other):
        #print("Parent eq is being called")
        return self.name == other.name and self.age == other.age 
    def __hash__(self):
        return hash((self.name,self.age))

class Child(Person):
    def __init__(self,name,age, selected_level, *args):
        super().__init__(name,age)
        self.educational_level =  {1:"Primary", 2:"Secondary", 3:"University"}
        self.selected_level = selected_level
        
    def __eq__(self,other):
        #print("Child eq is being called")
        return super().__eq__(other) and self.educational_level == other.educational_level
    
    def __hash__(self):
        return hash((self.name,self.age,self.selected_level))
    
p1 = Person("Paco", 36) #if p2 age was 37 and __eq__ method only what cheking age, result will still be true
p2 = Person("Paco", 36)#same has value than p1, but as latest, this one is being added 

c1 = Child("John", 36, 1)
c2 = Child("Michael", 36, 1)
c3 = Child("John", 36, 1,3) #this John is gonna be added only

print(p1 == p2)
print(c2 == c3)
#dict -- unique value is being replaced by latest
person_dict = {hash(p1):p1, hash(p2):p2, hash(c1):c1, hash(c2):c2, hash(c3):c3} #only unique values are being added (taking count the attributes that are being compared)
for key,obj in person_dict.items():
    print(f"Hash key:{key}")
    if hasattr(obj, 'selected_level'): 
        print(f"Object: {obj.__class__.__name__}, Name: {obj.name}, Age: {obj.age} , Selected level {obj.educational_level[obj.selected_level]} \n")
    else:
        print(f"Object: {obj.__class__.__name__}, Name: {obj.name}, Age: {obj.age} \n")
    
#Set - repeated hash values are not being added
person_list = [(hash(obj),obj) for obj in [p1,p2,c1,c2,c3]]
for key, obj in person_list:
    print(f"Class: {obj.__class__.__name__}: Names printed with a list (they repeating): {obj.name}")

person_set = set(person_list)
print("\n")
for key, obj in person_set:
    print(f"Class: {obj.__class__.__name__}: Names printed with a set (__hash__ in scene) {obj.name}") 
    
