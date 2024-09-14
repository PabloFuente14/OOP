#It all works through a class called RandomWord. This class is initiallized with a path to a word file, where is readig each word and adding them to a list of words.
#It prints num of words read
#It must not all of this be done in the constructor,, try to call methods in the cosntructor that make this job
#Include a child son called RandomChr that stores each char occurrence and gives a random char depending on such occurrences

import re
import pandas as pd
import random

class RandomWord():
    _words = []
    
    def __init__ (self,path, pattern=r'\b[a-zA-Z]+\b'):
      self.path = path
      self.pattern = pattern
      self.num_words = self.number_of_words_read()
     
        
    def number_of_words_read(self):
        RandomWord._words = open(self.path,"r").read().splitlines()
        df = pd.DataFrame(RandomWord._words, columns= ['words'])
        df = df[df['words'].str.contains(self.pattern, regex = True)]
        RandomWord._words = df['words'].to_list()
        return f"{len(df)} Words read" 
      
    def pick_random(self):
        return random.choice(RandomWord._words)
      
class RandomChar(RandomWord):
  def __init__ (self, path ):
    super().__init__(path,)
    self.char_counter = {}
    
  def counting_chars(self):
    for word in RandomWord._words:
      for char in word:
        if char not in self.char_counter:
          self.char_counter[char] = 1
        else:
          self.char_counter[char] += 1
    
    return self.char_counter
  
  def pick_random(self):
    chars = [key for key in self.char_counter]
    frequencies = [value for key,value in self.char_counter.items()]
    #pick one char setting the weights according to its frecquencies
    return random.choices(chars, weights=frequencies, k=1)[0]

      
if __name__ == '__main__':
  
  rand = RandomWord(r"E:\Python\OOP\OOProjects\RandWord\words2.txt")
  print(rand.num_words)
  print(rand.pick_random())
        
  randChar = RandomChar(r"E:\Python\OOP\OOProjects\RandWord\words2.txt")
  print(randChar.counting_chars())
  
  print(randChar.pick_random())
  print(randChar.num_words)
  


    