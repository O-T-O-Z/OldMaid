
"""
One world in the Kripke model. agent_hands should contain a list where each element
is a set of card values representing the cards that an agent has
"""
class World:

    def __init__(self, agent_hands):
        self.agent_hands = {}
        for i, hand in agent_hands:
            self.agent_hands[i] = hand

    def __repr__(self):
        return str(self.agent_hands)

    # evaluate an atomic sentence in this world
    def eval_atom(self, agent, value):
        return value in self.agent_hands[agent]