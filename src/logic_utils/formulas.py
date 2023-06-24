
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
        if not issubclass(type(formula), Sentence):
            exit("Complex formulas can only be constructed from other formulas")

    # returns the agent id of the agent the sentence is about. Do not use for complex sentences
    # about more than one agent (in the atoms, mixed agents in the epistemic connectives are fine)
    def owner_id(self):
        pass

"""
The class for an atomic sentence (no connectives in the sentence)
"""
class Atom(Sentence):

    def __init__(self, agent_id, card_value):
        self.agent_id = agent_id
        self.card = card_value

    def __str__(self) -> str:
        return str(self.agent_id) + " has " + str(self.card)

    def eval(self, world, model=None):
        return world.eval_atom(self.agent_id, self.card)
    
    def owner_id(self):
        return self.agent_id
    
    

"""
Negation connective
"""
class Neg(Sentence):

    def __init__(self, formula):
        self.assert_is_wff(formula)
        self.pos_formula = formula
        if isinstance(formula, Atom):
            self.agent_id = formula.agent_id
            self.card = formula.card
        else:
            self.agent_id = None
            self.card = None

    def __str__(self) -> str:
        return "not " + str(self.pos_formula)

    def eval(self, world, model=None):
        return 1 - self.pos_formula.eval(world, model)
    
    def owner_id(self):
        return self.pos_formula.owner_id()
    

"""
Disjunction connective, expects a list of formulas to for a disjunciton out of
"""
class Or(Sentence):

    def __init__(self, wffs):
        self.wffs = []
        for wff in wffs:
            self.assert_is_wff(wff)
            self.wffs.append(wff)

        if isinstance(wffs[0], K):
            self.agent_id = wffs[0].agent_id

    def eval(self, world, model=None):
        for wff in self.wffs:
            if wff.eval(world, model):
                return True
        return False    
    
    def owner_id(self):
        return self.wffs[0].owner_id()
        

"""
Epistemic 'K_i' connective, expects a formula and an agent which supposedly knows the formula 
"""
class K(Sentence):

    def __init__(self, agent_id, formula):
        self.assert_is_wff(formula)
        self.formula = formula
        self.agent_id = agent_id

    def eval(self, world, model):
        accessible_worlds = model.get_accessible_worlds(world, self.agent_id)
        for other_world in accessible_worlds:
            if not self.formula.eval(other_world, model):
                return False
        return True
    
    # knowing whether the agent knows a positive or a negative is useful for pruning epistemic sentences
    def knows_neg(self):
        return isinstance(self.formula, Neg)
    
    def owner_id(self):
        return self.formula.owner_id()
