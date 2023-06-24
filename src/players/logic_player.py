from .player import Player
import random
from logic_utils.formulas import *


class LogicPlayer(Player):

    def __init__(self, player_id):
        super().__init__(player_id)
        self.last_given_card = None
        self.knowledge = []

    def remove_contradictions(self, fact):
        # remove facts that are contradicted by the new knowledge
        for i, p in enumerate(self.knowledge):
            if (isinstance(p, Neg) or isinstance(p, Atom)) and p.agent_id == fact.agent_id and p.card == fact.card:
                self.knowledge.pop(i)
                break
        self.knowledge.append(fact)
    
    def prune_current_knowledge(self, drawing_player, giving_player, current_players, discarded):
        new_knowledge = []
        for atom in self.knowledge:
            # remove facts about players that are no longer in the game
            if atom.agent_id not in [p.id for p in current_players]:
                continue
            # remove positive facts about the giving player
            elif self.id not in [drawing_player.id, giving_player.id] and atom.agent_id == giving_player.id and not isinstance(atom, Neg):
                continue
            # remove negative facts about the drawing player
            elif self.id not in [drawing_player.id, giving_player.id] and atom.agent_id == drawing_player.id and isinstance(atom, Neg) and not discarded:
                continue
            new_knowledge.append(atom)
        return new_knowledge

    def add_basic_knowledge(self, drawing_player, giving_player, current_players, discarded):
        fact = None
        current_ids = [p.id for p in current_players]
        if self.id == giving_player.id and not discarded and drawing_player.id in current_ids:
            # agent now knows that the drawing player has the card that was given away
            fact = Atom(drawing_player.id, self.last_given_card)
        elif self.id == drawing_player.id and giving_player.id in current_ids:
            # agent now knows that the giving player does not have the card that was given away
            fact = Neg(Atom(giving_player.id, giving_player.last_given_card))
        elif self.id != drawing_player.id and discarded and drawing_player.id in current_ids:
            # agent now knows that the active player does not have the card that was discarded
            fact = Neg(Atom(drawing_player.id, discarded))

        if fact:
            # more efficient to do once here than in each of the above cases
            self.remove_contradictions(fact)
        if self.id not in [drawing_player.id, giving_player.id] and giving_player.id in current_ids and discarded:
            # agent now knows that the giving player does not have the card that was discarded
            # has to happen here because neutral players might know both from the drawing and the giving player
            # relevant to know when more than 3 players
            fact = Neg(Atom(giving_player.id, discarded))
            self.remove_contradictions(fact)

    def update_knowledge(self, drawing_player, giving_player, current_players, discarded):
        self.knowledge = self.prune_current_knowledge(drawing_player, giving_player, current_players, discarded)
        self.add_basic_knowledge(drawing_player, giving_player, current_players, discarded)

        print("Knowledge of player " + str(self.id) + ":")
        for value in self.knowledge:
            print(str(value))

    def choose_player(self, possible_players, model):
        # choose the player that 1) has the most of your hand and 2) has the most cards
        target_player = possible_players[0]
        possible_worlds = model.get_possible_worlds(self, self.knowledge)
        cards_common_with = {player.id: 0 for player in possible_players}
        print("Accessible worlds: " + str(possible_worlds))
        print("All worlds:")

        for world in model.worlds:
            print(world)
        for player in possible_players:
            for world in possible_worlds:
                # check in every world how many cards the player has common with each other player
                cards_common_with[player.id] += len(set(world.agent_hands[player.id]).intersection(set(self.hand)))
        print("Cards common with: " + str(cards_common_with))
        # choose the player with the most cards in common with you
        max_common = 0
        for player in possible_players:
            if cards_common_with[player.id] > max_common:
                target_player = player
                max_common = cards_common_with[player.id]
            elif cards_common_with[player.id] == max_common:
                # if there is a tie, choose the player with the most cards
                if len(player.hand) > len(target_player.hand):
                    target_player = player
        return target_player

    # your turn, choose a player and which card to take
    def choose_card(self, possible_players, model):
        target_player = self.choose_player(possible_players, model)
        print("Target player: " + str(target_player.id))

        available_cards = target_player.present_hand()
        target_card = random.randint(0, available_cards - 1)

        return target_player, target_card
    