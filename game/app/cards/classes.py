import re
import numpy as np

class Card:
    def __init__(self, text):
        self.text = self.clean_text(text)
        
    def clean_text(self, text):
        ''' 
        Clean text body by: \n
        - Captializing sentence\n
        - Removing excess spaces at end \n
        - Adding period if missing @ end
        '''
        
        text = text.capitalize()
        text = text.replace("\n", "")
        text = text.rstrip()
        
        ending_punctuation = [".", "!", "?"]
        results = [p in text[-5:] for p in ending_punctuation]
        if True not in results:
            text += "."
        
        return text

class BlackCard(Card):
    def __init__(self, text):
        super().__init__(text)
        self.blanks = -1
        self.clean()
    
    def __callback(self, match):
        self.blanks += 1
        return "{" + str(self.blanks) + "}"

    def clean(self):
        self.blanks = 0
        if "__" in self.text:
            matches = re.sub("_*_", self.__callback, self.text)
        else:
            self.text += " {0}."
            self.blanks = 1
    
    def fill_in(self, white_cards):
        return self.text.format(*white_cards)
    
class CardSet:
    
    def __init__(self, strings):
        self.strings = strings
    
    def get_random_card(self, range_= ()):
    
        if len(range_) < 1:
            # Use entire range if none given
            range_ = (0, len(self.strings)-1)
            
        i = np.random.randint(range_[0], range_[1])
        return self.strings[i]