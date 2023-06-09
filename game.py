import random

from player import Player
from deck import Deck

card_types = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]

class Game():

    def __init__(self, num_players):
        # init players
        self.players = []
        for i in range(num_players):
            player = Player(player_id=i, card_types=card_types)
            self.players.append(player)

        # init deck and hand out cards
        deck = Deck(card_types)
        idx = 0
        while not deck.is_empty():
            self.players[idx].receive_card(deck.draw())
            idx = (idx + 1) % num_players

    
    def run(self):
        turn = random.randint(0, len(self.players) - 1)

        while True:
            # current player chooses a move
            active_player = self.players[turn]
            target_player_idx, chosen_card = active_player.choose_card(self.players)
            target_player = self.players[target_player_idx]

            # the move gets executed, some announcements should happen here
            active_player.receive_card(target_player.give_card(chosen_card))

            # check if any players are out
            if len(active_player.hand) == 0:
                self.players.pop(turn)
                turn -= 1
            if len(target_player.hand) == 0:
                self.players.pop(target_player_idx)

            # check if the game is over
            if len(self.players) == 1:
                break

            # next player's turn
            turn = (turn + 1) % len(self.players)

        loser = self.players[0].player_id
        print(f"Game is over. Player {loser} is the old maid!")

        return loser

            

