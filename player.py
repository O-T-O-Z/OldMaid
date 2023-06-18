import random

from logic_utils.formulas import *
from logic_utils.world import *

class Player():

    def __init__(self, player_id, card_types):
        self.player_id = player_id
        self.hand = []
        self.knowledge = {}
        for card_type in card_types:
            self.knowledge[card_type] = set()


    # receive a card and check if you have any pairs
    def receive_card(self, new_card):
        # need to fix this
        self.knowledge[new_card.type].add(new_card.id)
        for idx, card in enumerate(self.hand):
            if card.type == new_card.type:
                # match found! discard and announce
                self.hand.pop(idx)
                return
        self.hand.append(new_card)


    # show another player how many cards you have so they can pick one
    def present_hand(self):
        return len(self.hand)


    # give another player one of your cards
    def give_card(self, card_idx):
        return self.hand.pop(card_idx)
        

    # your turn, choose a player and which card to take
    def choose_card(self, active_players):
        target_player_idx = random.randint(0, len(active_players) - 1) # implement choosing
        target_player = active_players[target_player_idx]
        available_cards = target_player.present_hand()
        target_card = random.randint(0, available_cards - 1) # implement choosing

        return target_player_idx, target_card




    
