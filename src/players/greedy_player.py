from .player import Player
import random

class GreedyPlayer(Player):
    def __init__(self, player_id):
        super().__init__(player_id)

    # your turn, choose the player with the most cards
    def choose_card(self, active_players):
        target_player = max(active_players, key=lambda x: x.present_hand())
        available_cards = target_player.present_hand()
        target_card = random.randint(0, available_cards - 1)

        return target_player, target_card