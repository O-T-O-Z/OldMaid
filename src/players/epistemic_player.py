from .logic_player import LogicPlayer
from logic_utils.formulas import *


class EpistemicPlayer(LogicPlayer):
    
    def __init__(self, player_id):
        super().__init__(player_id)
    
    def update_knowledge(self, drawing_player, giving_player, current_players, discarded):
        self.knowledge = self.prune_current_knowledge(drawing_player, giving_player, current_players, discarded)
        self.add_basic_knowledge(drawing_player, giving_player, current_players, discarded)

        print("Knowledge of player " + str(self.id) + ":")
        for value in self.knowledge:
            print(str(value))

    def add_epistemic_knowledge(self, drawing_player, giving_player, current_players, discarded, card_types):
        if not discarded and self.id != drawing_player.id and self.id != giving_player.id:
            fact1 = Or([K(giving_player.id, Atom(drawing_player.id, card)) for card in card_types])
            fact2 = Or([K(drawing_player.id, Atom(drawing_player.id, card)) for card in card_types])
            self.knowledge.append(fact1)
            self.knowledge.append(fact2)