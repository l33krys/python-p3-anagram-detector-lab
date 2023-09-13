# your code goes here!

class Anagram:

    def __init__(self, word):
        self.word = word
    
    def match(self, list):
      matches = []
      for item in list:
        letters = [letter for letter in item]
        if sorted(self.word) == sorted(letters):
          matches.append(item)
      return matches