
"""
General abstract class for logical sentences which all connectives inherit from
"""
class Sentence():

    def __init__(self):
        pass

    # The world is needed to evaluate any sentence, the model only needs to be specified if there are
    # modal connectives in the sentence
    def eval(self, world, model=None):
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

    def eval(self, world, model=None):
        return world.eval_atom(self.agent_id, self.card)
    

"""
Negation connective
"""
class Neg(Sentence):

    def __init__(self, formula):
        self.assert_is_wff(formula)
        self.pos_formula = formula

    def eval(self, world, model=None):
        return 1 - self.pos_formula.eval(world, model)
    

"""
Disjunction connective, expects a list of formulas to for a disjunciton out of
"""
class Or(Sentence):

    def __init__(self, wffs):
        self.wffs = []
        for wff in wffs:
            self.assert_is_wff(wff)
            self.wffs.append(wff)

    def eval(self, world, model=None):
        for wff in self.wffs:
            if wff.eval(world, model):
                return True
        return False    
        

"""
Epistemic 'K_i' connective, expects a formula and an agent which supposedly knows the formula 
"""
class K(Sentence):

    def __init__(self, formula, agent_id):
        self.assert_is_wff(formula)
        self.formula = formula
        self.agent_id = agent_id

    def eval(self, world, model):
        accessible_worlds = model.get_accessible_worlds(world, self.agent_id)
        for other_world in accessible_worlds:
            if not self.formula.eval(other_world, model):
                return False
        return True

