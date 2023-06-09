

class WorldConstructor():

    def __init__(self, card_ids, card_types, agents):
       atoms = []
       for card_type in card_types:
           atoms += [str(card_id) + ':' + card_type for card_id in card_ids] 

    
        