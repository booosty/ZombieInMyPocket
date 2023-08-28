class Item:
    def __init__(self, name, action, uses, combinable, combines_with, makes, action_amount=0):
        self.name = name
        self.action = action
        self.uses = uses
        self.combinable = combinable
        self.combines_with = combines_with
        self.makes = makes
        self.action_amount = action_amount
