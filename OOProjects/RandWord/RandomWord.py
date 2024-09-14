#It all works through a class called RandomWord. This class is initiallized with a path to a word file, where is readig each word and adding them to a list of words.
#It prints num of words read
#It must not all of this be done in the constructor,, try to call methods in the cosntructor that make this job
#This class provides a random() method that returns a random word from the list of words
import pandas as pd
import random

class RandomWord():
    _words = []
    def __init__ (self,path):
      self.path = path
      self.num_words = self.number_of_words_read()
      
    
    def number_of_words_read(self):
        RandomWord._words = open(self.path,"r").read().splitlines()
        df = pd.DataFrame(RandomWord._words)
        print(f"{len(df)} words read") 
        
    def pick_random(self):
        return random.choice(RandomWord._words)
      
      
if __name__ == '__main__':
        
  rand = RandomWord(r"E:\Python\OOP\OOProjects\python-oo-practice\python-oo-practice\words.txt")
  
  print(rand.pick_random())

    