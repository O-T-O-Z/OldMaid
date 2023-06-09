import random

from card import Card

card_types = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]

class Deck():

    def __init__(self):
        # build and shuffle the deck
        self.cards = []
        count = 0
        for card_type in card_types:
            amount = (3 if card_type == 'queen' else 4)
            for _ in range(amount):
                new_card = Card(card_type, count)
                self.cards.append(new_card)

                count += 1

        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop(0)

    def is_empty(self):
        return len(self.cards) == 0
        
        
    
