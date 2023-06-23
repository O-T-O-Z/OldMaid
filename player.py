import random

from logic_utils.formulas import *
from logic_utils.world import *

class Player:

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
    
    def update_knowledge(self, drawing_player, giving_player):
        if self.id not in [drawing_player.id, giving_player.id]:
            # agent does not know anything about the player that has given a card now
            if giving_player.id in self.knowledge["given_cards"]:
                self.knowledge["cards_of_player"][giving_player.id] = []
        elif self.id == giving_player.id:
            # agent now knows that the target player has the card that was given away
            self.knowledge["cards_of_player"][giving_player.id].append(Atom(self.id, self.last_given_card))
        elif self.id == drawing_player.id:
            # agent now knows that the active player does not have the card that was given away
            self.knowledge["cards_of_player"][drawing_player.id].append(Neg(self.last_given_card))

    # your turn, choose a player and which card to take
    def choose_card(self, active_players, model):
        # TODO: use model to choose a card
        target_player = random.choice(active_players) # implement choosing
        available_cards = target_player.present_hand()
        target_card = random.randint(0, available_cards - 1) # implement choosing

        return target_player, target_card




    
