
"""
One world in the Kripke model. agent_hands should contain a list where each element
is a set of card values representing the cards that an agent has
"""
class World():

    def __init__(self, world_id, agent_hands):
        self.id = world_id
        self.agent_hands = agent_hands

    # evaluate an atomic sentence in this world
    def eval_atom(self, agent, value):
        return value in self.agent_hands[agent]