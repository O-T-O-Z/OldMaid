
"""
General abstract class for logical sentences which all connectives inherit from
"""
class Sentence():

    def __init__(self):
        pass

    def eval(self, world):
        pass

    def assert_is_wff(self, formula):
        if not issubclass(formula, Sentence):
            exit("Complex formulas can only be constructed from other formulas")

"""
The class for an atomic sentence (no connectives in the sentence)
"""
class Atom(Sentence):

    def __init__(self, agent_id, card_value):
        self.agent_id = agent_id
        self.card = card_value

    def eval(self, world):
        return world.eval_atom(self.agent_id, self.card)
    

"""
Negation connective
"""
class Neg(Sentence):

    def __init__(self, formula):
        self.assert_is_wff(formula)
        self.pos_formula = formula

    def eval(self, world):
        return 1 - self.pos_formula.eval(world)
    

"""
Disjunction connective, expects a list of formulas to for a disjunciton out of
"""
class Or(Sentence):

    def __init__(self, wffs):
        self.wffs = []
        for wff in wffs:
            self.assert_is_wff(wff)
            self.wffs.append(wff)

    def eval(self, world):
        for wff in self.wffs:
            if wff.eval(world):
                return True
        return False    
        

