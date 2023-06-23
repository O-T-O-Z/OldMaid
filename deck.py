import random

class Deck:

    def __init__(self, card_types):
        # build and shuffle the deck
        self.cards = []
        for card_type in card_types:
            amount = (3 if card_type == 'Q' else 4)
            for _ in range(amount):
                self.cards.append(card_type)

        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop(0)

    def is_empty(self):
        return len(self.cards) == 0
        
        
    
