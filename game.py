import random

from player import Player
from deck import Deck
from model import Model

card_types = ["J", "Q", "K", "A", "B"]

class Game:

    def __init__(self, num_players):
        # init players
        self.players = []
        for i in range(num_players):
            player = Player(player_id=i)
            self.players.append(player)

        # init deck and hand out cards
        deck = Deck(card_types)
        idx = 0
        while not deck.is_empty():
            self.players[idx].receive_card(deck.draw())
            idx = (idx + 1) % num_players
        for player in self.players:
            if not player.hand:
                print(f"Player {player.id} is out!")
                self.players.pop(player.id)
        # init model
        self.model = Model()
        self.model.update_model(self.players)

    
    def run(self):
        active_player = random.choice(self.players)

        while True:
            print("=====================================")
            print(f"Player {active_player.id}'s turn")
            # current player chooses a move
            possible_players = [player for player in self.players if player.id != active_player.id]
            target_player, chosen_card = active_player.choose_card(possible_players, self.model)

            # the move gets executed, some announcements should happen here
            active_player.receive_card(target_player.give_card(chosen_card))

            # check if any players are out
            if len(active_player.hand) == 0:
                print(f"Player {active_player.id} is out!")
                self.players.remove(active_player)
            if len(target_player.hand) == 0:
                print(f"Player {target_player.id} is out!")
                self.players.remove(target_player)

            # check if the game is over
            if len(self.players) == 1:
                break
            # update model
            self.model.update_model(self.players)
            # self.announce_move(active_player, target_player, self.model.card_counts)

            # next player's turn
            for p in filter(lambda x: x.id != active_player.id, self.players):
                if p.id > active_player.id:
                    active_player = p
                    break
            else:
                active_player = next(filter(lambda x: x.id != active_player.id, self.players))

        loser = self.players[0].id
        print(f"Game is over. Player {loser} is the old maid!")

        return loser


    def announce_move(self, active_player, target_player):
        print(f"Player {active_player.id} took a card from player {target_player.id}")
        for player in self.players:
            player.update_knowledge(active_player, target_player)

