from logic_utils.formulas import *
from logic_utils.world import *
from abc import ABC, abstractmethod

class Player(ABC):

    def __init__(self, player_id, verbose=False):
        self.id = player_id
        self.hand = []
        self.last_given_card = None
        self.knowledge = []
        self.verbose = verbose

    # receive a card and check if you have any pairs
    def receive_card(self, new_card):
        for idx, card in enumerate(self.hand):
            if card == new_card:
                # match found! discard and announce
                if self.verbose:
                    print(f"Player {self.id} discarded a pair of {new_card}")
                self.hand.pop(idx)
                return new_card
        self.hand.append(new_card)
        return None


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