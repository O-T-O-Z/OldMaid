from .player import Player
import random
from logic_utils.formulas import *

class EpistPlayer(Player):

    def __init__(self, player_id, num_cards):
        super.__init__(player_id)
        
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