from .player import Player
import random

class RandomPlayer(Player):
    def __init__(self, player_id):
        super().__init__(player_id)

    # your turn, choose a player and which card to take
    def choose_card(self, active_players, model):
        target_player = random.choice(active_players)
        available_cards = target_player.present_hand()
        target_card = random.randint(0, available_cards - 1)

        return target_player, target_card
    
    # random player has no knowledge
    def update_knowledge(self, drawing_player=None, giving_player=None, current_players=None, discarded=None, card_types=None):
        pass