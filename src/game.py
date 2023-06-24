import random

from players import RandomPlayer, EpistemicPlayer, LogicPlayer
from deck import Deck
from model import Model

card_types = ["J", "Q", "K", "A", "B"]

class Game:

    def __init__(self, num_players):
        # init players
        self.players = []
        for i in range(num_players):
            player = EpistemicPlayer(player_id=i)
            self.players.append(player)

        # init deck and hand out cards
        deck = Deck(card_types)
        idx = 0
        while not deck.is_empty():
            self.players[idx].receive_card(deck.draw())
            idx = (idx + 1) % num_players
        
        # remove players with empty hands
        self.players = [player for player in self.players if player.hand]

        # init model
        self.model = Model()
        self.model.update_model(self.players)

    
    def run(self):
        active_player = random.choice(self.players)

        while True:
            print("=====================================")
            # print(f"Player {active_player.id}'s turn")
            # current player chooses a move
            possible_players = [player for player in self.players if player.id != active_player.id]
            target_player, chosen_card = active_player.choose_card(possible_players, self.model)

            # the move gets executed, some announcements should happen here
            given_card = target_player.give_card(chosen_card)
            print(f"Player {active_player.id} received a {given_card} from player {target_player.id}")
            discarded = active_player.receive_card(given_card)

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
            self.announce_move(active_player, target_player, discarded)

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


    def announce_move(self, active_player, target_player, discarded):
        for player in self.players:
            player.update_knowledge(active_player, target_player, self.players, discarded=discarded)

