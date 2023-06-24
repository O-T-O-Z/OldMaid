from .player import Player
import random

class RandomPlayer(Player):
    def __init__(self, player_id):
        super().__init__(player_id)

    # your turn, choose a player and which card to take
    def choose_card(self, active_players):
        # TODO: use model to choose a card
        target_player = random.choice(active_players) # implement choosing
        available_cards = target_player.present_hand()
        target_card = random.randint(0, available_cards - 1) # implement choosing

        return target_player, target_card