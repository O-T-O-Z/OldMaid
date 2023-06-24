import random

from logic_utils.formulas import *
from logic_utils.world import *
from abc import ABC, abstractmethod

class Player(ABC):

    def __init__(self, player_id):
        self.id = player_id
        self.hand = []
        self.last_given_card = None
        # an agent knows how many cards each player has, 
        # how many cards of each type there are, 
        # and which cards some players have through giving away or receiving
        self.knowledge = {"cards_of_player": {}}


    # receive a card and check if you have any pairs
    def receive_card(self, new_card):
        # need to fix this
        # self.knowledge[new_card].add(new_card.id)
        print(f"Player {self.id} received a {new_card}")
        for idx, card in enumerate(self.hand):
            if card == new_card:
                # match found! discard and announce
                print(f"Player {self.id} discarded a pair of {new_card}")
                self.hand.pop(idx)
                return
        self.hand.append(new_card)


    # show another player how many cards you have so they can pick one
    def present_hand(self):
        return len(self.hand)

    def give_card(self, card_idx):
        # give another player one of your cards
        self.last_given_card = self.hand[card_idx]
        return self.hand.pop(card_idx)
    
    @abstractmethod
    def choose_card(self, active_players, *args, **kwargs):
        raise NotImplementedError