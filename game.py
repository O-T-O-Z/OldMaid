import random

from player import Player
from deck import Deck
from model import Model

card_types = ["J", "Q", "K"]

class Game:

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

        # init model
        self.model = Model()
        self.model.update_model(self.players)
        exit()

    
    def run(self):
        active_player_idx = random.randint(0, len(self.players) - 1)

        while True:
            # current player chooses a move
            active_player = self.players[active_player_idx]
            target_player_idx, chosen_card = active_player.choose_card(self.players, self.model)
            target_player = self.players[target_player_idx]

            # the move gets executed, some announcements should happen here
            active_player.receive_card(target_player.give_card(chosen_card))

            # check if any players are out
            if len(active_player.hand) == 0:
                self.players.pop(active_player_idx)
                active_player_idx -= 1
            if len(target_player.hand) == 0:
                self.players.pop(target_player_idx)

            # check if the game is over
            if len(self.players) == 1:
                break
            
            # update model
            self.model.update_model(self.players)
            self.announce_move(active_player, target_player, self.model.card_counts)

            # next player's turn
            active_player_idx = (active_player_idx + 1) % len(self.players)

        loser = self.players[0].player_id
        print(f"Game is over. Player {loser} is the old maid!")

        return loser

    def announce_move(self, active_player, target_player, card_counts):
        print(f"Player {active_player.player_id} took a card from player {target_player.player_id}")
        for player in self.players:
            player.update_knowledge(active_player, target_player, card_counts)

