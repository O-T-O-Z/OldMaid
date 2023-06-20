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
        self.worlds = {} # {world_id: [p1_state, p2_state, ...]}
        self.relations = {} # {player_id: [world_id, ...]}
    
    def update_model(self, players):
        # count all cards and types in the game
        self.count_cards(players)
        print(self.card_counts)

        # these are the possible worlds
        self.get_possible_worlds()
        print(self.worlds)

        # now get the relations that each player considers possible given their hand and knowledge
        self.get_relations()
        print(self.relations)

    def count_cards(self, players):
        for player in players:
            self.cards += player.hand
        for card in self.cards:
            self.card_counts[card.type] = self.card_counts.get(card.type, 0) + 1

    def get_possible_worlds(self):
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
        pass
    
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
    
