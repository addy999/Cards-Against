import shortuuid
from .classes import *

class GameSession:
    
    def __init__(self, black_cards=CardSet, white_cards=CardSet, id_len=5):

        self.black_cards = black_cards
        self.white_cards = white_cards
        self.id = shortuuid.ShortUUID().random(length=id_len)
    
    
    
        
    