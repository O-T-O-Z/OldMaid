import itertools
from logic_utils.world import World
import numpy as np
# Example:
# 3 players, 3 card types
# player 1: 1, 2, 1, 3 
# player 2: 2, 3, 1, 2
# player 3: 1, 3, 2, 3

# After discarding:
# player 1: 2, 3
# player 2: 1, 3
# player 3: 1, 2

# Possible worlds:
#         P1      P2      P3
# {
#   1: [(1, 3), (1, 2), (2, 3)],
#   2: [(1, 3), (2, 3), (1, 2)],
#   3: [(1, 2), (1, 3), (2, 3)],
#   4: [(1, 2), (2, 3), (1, 3)],
#   5: [(2, 3), (1, 3), (1, 2)], -> TRUE
#   6: [(2, 3), (1, 2), (1, 3)],
# }

class Model:

    def __init__(self):
        self.cards = [] # [card1, card2, ...]
        self.card_counts = {} # {card_type: count}
        self.worlds = [] # {world_id: [p1_state, p2_state, ...]}
        self.hand_sizes = {} # {player_id: hand_size}
    
    def update_model(self, players):
        print(f"True world: {[(player.id, player.hand) for player in players]}")
        # count all cards and types in the game
        self.count_cards(players)
        print(f"Card counts: {self.card_counts}")

        # these are the possible worlds
        self.create_possible_worlds()
        print("Possible worlds:")
        for world in self.worlds:
            print(world)

    def count_cards(self, players):
        self.card_counts = {}
        self.cards = []
        self.hand_sizes = {}
        for player in players:
            self.cards += player.hand
            self.hand_sizes[player.id] = len(player.hand)
        for card in self.cards:
            self.card_counts[card] = self.card_counts.get(card, 0) + 1

    # an agent cannot distinguish worlds where the agent's own hand is the same
    def exists_relation(self, agent_id, world1, world2):
        return world1.agent_hands[agent_id] == world2.agent_hands[agent_id]
        

    def create_possible_worlds(self):
        """
        Appends to the list of all possible worlds self.worlds given the current game state.

        This uses the card counts to determine which worlds are possible given that:
        - the number of players is known
        - the number of cards per player is known
        - the number of cards per type is known

        Do not consider worlds that are not possible because they:
        - contain pairs
        - are identical: 1,2 <-> 2,1
        """
        # TODO
        card_perms = itertools.permutations(self.cards)
        worlds = []
        for perm in list(card_perms):
            hands = []
            card_idx = 0
            for hand_size in self.hand_sizes.values():
                hand = set(perm[card_idx:(card_idx + hand_size)])
                card_idx += hand_size
                # We know the hand size, so if the permutation has fewer cards, it is not a possibility
                if len(hand) < hand_size:
                    break
                hands.append(hand)
            else:
                if hands not in worlds:
                    worlds.append(hands)
 
        self.worlds = [World(w) for w in worlds]
