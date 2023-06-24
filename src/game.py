import random

from players import RandomPlayer, EpistemicPlayer, LogicPlayer
from deck import Deck
from model import Model

CARD_TYPES = ["J", "Q", "K", "A"]

class Game:

    """
    Game has 3 conditions:
    0: basic logical agent playing against random agents
    1: epistemic agent playing against random agents
    2: epistemic agent playing against basic logical agents
    """
    def __init__(self, num_players, condition=0, verbose=False):
        # init players
        if condition not in [0, 1, 2]:
            exit("Unknown game setup condition. Choose from 0, 1, and 2")
        self.players = []
        self.verbose=verbose

        # determine which kinds of agents will play
        main_player_class = (LogicPlayer if condition == 0 else EpistemicPlayer)
        other_player_class = (LogicPlayer if condition == 2 else RandomPlayer)

        # init agents
        main_player = main_player_class(player_id=0, verbose=verbose)
        self.players.append(main_player)
        for i in range(1, num_players):
            player = other_player_class(player_id=i, verbose=verbose)
            self.players.append(player)

        # init deck and hand out cards
        deck = Deck(CARD_TYPES)
        idx = random.randint(0, num_players - 1)
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
            if self.verbose:
                print("=====================================")
            # print(f"Player {active_player.id}'s turn")
            # current player chooses a move
            possible_players = [player for player in self.players if player.id != active_player.id]
            target_player, chosen_card = active_player.choose_card(possible_players, self.model)

            # the move gets executed, some announcements should happen here
            given_card = target_player.give_card(chosen_card)
            if self.verbose:
                print(f"Player {active_player.id} received a {given_card} from player {target_player.id}")
            discarded = active_player.receive_card(given_card)

            # check if any players are out
            if len(active_player.hand) == 0:
                if self.verbose:
                    print(f"Player {active_player.id} is out!")
                self.players.remove(active_player)
            if len(target_player.hand) == 0:
                if self.verbose:
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
        if self.verbose:
            print(f"Game is over. Player {loser} is the old maid!")

        return loser


    def announce_move(self, active_player, target_player, discarded):
        for player in self.players:
            player.update_knowledge(active_player, target_player, self.players, discarded, self.model.card_counts.keys())

