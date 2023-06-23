import itertools
from logic_utils.world import World
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

# Possible relations (given their own hand):
# {player1: [5,6], player2: [1,2], player3: [3,4]}

class Model:

    def __init__(self):
        self.cards = [] # [card1, card2, ...]
        self.card_counts = {} # {card_type: count}
        self.worlds = [] # {world_id: [p1_state, p2_state, ...]}
        self.hand_sizes = []
        ## might not be used
        #self.relations = {} # {player_id: [world_id, ...]}
    
    def update_model(self, players):
        # count all cards and types in the game
        self.count_cards(players)
        print(self.card_counts)

        # these are the possible worlds
        self.create_possible_worlds()
        #print(self.worlds)

        # now get the relations that each player considers possible given their hand and knowledge
        #self.get_relations()
        #print(self.relations)

    def count_cards(self, players):
        self.hand_sizes = [0] * len(players)
        for player in players:
            self.cards += [card.type for card in player.hand]
            self.hand_sizes[player.player_id] = len(player.hand)
        for card in self.cards:
            self.card_counts[card.type] = self.card_counts.get(card.type, 0) + 1

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
        worlds = set()
        for perm in list(card_perms):
            print(perm)
            hands = []
            card_idx = 0
            for hand_size in self.hand_sizes:
                hand = set(perm[card_idx:(card_idx + hand_size)])
                card_idx += hand_size
                # We know the hand size, so if the permutation has fewer cards, it is not a possibility
                if len(hand) < hand_size:
                    break
                hands.append(tuple(hand))
            else:
                worlds.add(tuple(hands))

        for world_tuple in worlds:
            self.worlds.append(World([set(pl_hand) for pl_hand in list(world_tuple)]))
        
    
    # not needed
    def get_relations(self):
        """
        Appends to the list of all possible relations self.relations given the current game state.

        This uses the possible worlds to determine which relations are possible given that:
        - the player knows their own hand, so only considers worlds where their hand is true
        - the player knows the number of cards per type
        - the player knows the number of cards per player
        - the player knows some cards that other players have due to trading
        """
        # TODO
        pass
    
