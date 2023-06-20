

class WorldConstructor():

    def __init__(self, players):
        self.cards = []
        self.worlds = []
        self.relations = []
        for player in players:
            self.cards += player.hand
        self.init_model()
    
    def init_model(self):
        # count all cards and types in the game
        # create dictionary with card_type: count
        self.card_counts = {}
        for card in self.cards:
            self.card_counts[card.type] = self.card_counts.get(card.type, 0) + 1
        print(self.card_counts)

        # these are the possible worlds
        self.worlds = self.get_combinations()
        print(self.worlds)

        # now get the relations that each player considers possible given their hand and knowledge
        self.relations = self.get_relations()
        print(self.relations)

    
    def get_combinations(self):
        # make all possible combinations of cards and types given the number of players and card counts
        # remove all combinations that are not possible because they contain pairs or are identical: 1,2 <-> 2,1
        # TODO
        pass
    
    def get_relations(self):
        # TODO
        pass
    
# Example:
# 3 players, 3 card types
# player 1: 1, 2, 1, 2 
# player 2: 2, 3, 1, 3
# player 3: 1, 3, 2, 3

# After discarding:
# player 1: done
# player 2: 2, 1
# player 3: 1, 2