import random

from logic_utils.formulas import *
from logic_utils.world import *

class Player:

    def __init__(self, player_id, card_types):
        self.player_id = player_id
        self.hand = []
        self.last_given_card = None
        # an agent knows how many cards each player has, 
        # how many cards of each type there are, 
        # and which cards some players have through giving away or receiving
        self.knowledge = {"cards_per_player": {}, "card_counts": {}, "cards_of_player": {}}
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

    def give_card(self, card_idx):
        # give another player one of your cards
        self.last_given_card = self.hand[card_idx]
        return self.hand.pop(card_idx)
    
    def update_knowledge(self, active_player, target_player, card_counts):
        if self.player_id not in [active_player.player_id, target_player.player_id]:
            self.knowledge["cards_per_player"][active_player.player_id] = active_player.present_hand()
            self.knowledge["cards_per_player"][target_player.player_id] = target_player.present_hand()
            self.knowledge["card_counts"] = card_counts

            # agent does not know anything about the player that has given a card now
            if active_player.player_id in self.knowledge["given_cards"]:
                self.knowledge["cards_of_player"][active_player.player_id] = []
        elif self.player_id == active_player.player_id:
            # agent now knows that the target player has the card that was given away
            self.knowledge["cards_of_player"][target_player.player_id].append(Atom(self.last_given_card.type))
        elif self.player_id == target_player.player_id:
            # agent now knows that the active player does not have the card that was given away
            self.knowledge["cards_of_player"][active_player.player_id].append(Neg(self.last_given_card.type))

    # your turn, choose a player and which card to take
    def choose_card(self, active_players, model):
        # TODO: use model to choose a card
        target_player_idx = random.randint(0, len(active_players) - 1) # implement choosing
        target_player = active_players[target_player_idx]
        available_cards = target_player.present_hand()
        target_card = random.randint(0, available_cards - 1) # implement choosing

        return target_player_idx, target_card




    
