from .logic_player import LogicPlayer
from logic_utils.formulas import *


class EpistemicPlayer(LogicPlayer):

    def __init__(self, player_id, verbose=False):
        super().__init__(player_id, verbose=verbose)

    def update_knowledge(self, drawing_player, giving_player, current_players,
                         discarded, card_types):
        self.knowledge = self.prune_current_knowledge(drawing_player,
                                                      giving_player,
                                                      current_players,
                                                      discarded)
        self.add_basic_knowledge(drawing_player, giving_player, current_players,
                                 discarded)
        self.add_epistemic_knowledge(drawing_player, giving_player,
                                     current_players, discarded, card_types)

        if self.verbose:
            print("Knowledge of player " + str(self.id) + ":")
            for value in self.knowledge:
                print(str(value))

    def check_bonus_conditions(self, wff, drawing_player, giving_player,
                               current_players, discarded):
        if isinstance(wff, Or):
            # remove positive epistemic facts about the giving player
            if wff.wffs[0].agent_id not in [agent.id for agent in
                                            current_players]:
                return True
            elif self.id not in [drawing_player.id,
                                 giving_player.id] and wff.owner_id() == giving_player.id and not \
            wff.wffs[0].knows_neg():
                return True
            # remove negative facts about the drawing player
            elif self.id not in [drawing_player.id,
                                 giving_player.id] and wff.owner_id() == drawing_player.id and \
                    wff.wffs[0].knows_neg() and not discarded:
                return True

    def add_epistemic_knowledge(self, drawing_player, giving_player,
                                current_players, discarded, card_types):
        if not discarded and self.id != drawing_player.id and self.id != giving_player.id and giving_player in current_players:
            self.knowledge.append(
                Or([K(giving_player.id, Atom(drawing_player.id, card)) for card
                    in card_types]))
            self.knowledge.append(
                Or([K(drawing_player.id, Neg(Atom(giving_player.id, card))) for
                    card in card_types]))
