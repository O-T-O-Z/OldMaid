from .player import Player
import random
from logic_utils.formulas import *

class EpistPlayer(Player):

    def __init__(self, player_id):
        super().__init__(player_id)
    
    def remove_contradictions(self, fact):
        # remove facts that are contradicted by the new knowledge
        for i, p in enumerate(self.knowledge):
            if p.agent_id == fact.agent_id and p.card == fact.card:
                self.knowledge.pop(i)
                break
        self.knowledge.append(fact)

    def update_knowledge(self, drawing_player, giving_player, current_players, discarded):
        new_knowledge = []
        for atom in self.knowledge:
            # remove facts about players that are no longer in the game
            if atom.agent_id not in [p.id for p in current_players]:
                continue
            # remove positive facts about the giving player
            elif self.id not in [drawing_player.id, giving_player.id] and atom.agent_id == giving_player.id and not isinstance(atom, Neg):
                continue
            # remove negative facts about the drawing player
            elif self.id not in [drawing_player.id, giving_player.id] and atom.agent_id == drawing_player.id and isinstance(atom, Neg):
                continue
            new_knowledge.append(atom)
        self.knowledge = new_knowledge

        fact = None
        if self.id == giving_player.id and not discarded and drawing_player.id in [p.id for p in current_players]:
            # agent now knows that the drawing player has the card that was given away
            fact = Atom(drawing_player.id, self.last_given_card)
        elif self.id == drawing_player.id and giving_player.id in [p.id for p in current_players]:
            # agent now knows that the giving player does not have the card that was given away
            fact = Neg(Atom(giving_player.id, giving_player.last_given_card))
        elif self.id != drawing_player.id and discarded and drawing_player.id in [p.id for p in current_players]:
            # agent now knows that the active player does not have the card that was discarded
            fact = Neg(Atom(drawing_player.id, discarded))

        if fact:
            # more efficient to do once here than in each of the above cases
            self.remove_contradictions(fact)
        if self.id not in [drawing_player.id, giving_player.id] and giving_player.id in [p.id for p in current_players] and discarded:
            # agent now knows that the giving player does not have the card that was discarded
            # has to happen here because neutral players might know both from the drawing and the giving player
            # relevant to know when more than 3 players
            fact = Neg(Atom(giving_player.id, discarded))
            self.remove_contradictions(fact)

        print("Knowledge of player " + str(self.id) + ": " + str(self.knowledge))
        for value in self.knowledge:
            print(str(value))

    # your turn, choose a player and which card to take
    def choose_card(self, active_players, model):
        # TODO: use model to choose a card
        target_player = random.choice(active_players) # implement choosing
        available_cards = target_player.present_hand()
        target_card = random.randint(0, available_cards - 1) # implement choosing

        return target_player, target_card
        # among the cards in your hand, see which ones are more common (max count)
        common_cards = []
        max_count = 0
        for card in self.hand:
            if model.card_counts[card] > max_count:
                common_cards = [card]
                max_count = model.card_counts[card]
            elif model.card_counts[card] == max_count:
                common_cards.append(card)

        # choose a player that is most likely to have a card that you need
        # based on the possible worlds in the restricted model
        target_player = None
        max_w_cards = 0
        for player in active_players:
            w_cards = 0
            for world in model.worlds:
                for card in common_cards:
                    if card in world.agent_hands[player.id]:
                        w_cards += 1
            if w_cards > max_w_cards:
                max_w_cards = w_cards
                target_player = player

        available_cards = target_player.present_hand()
        target_card = random.randint(0, available_cards - 1)

        return target_player, target_card