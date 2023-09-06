class Card():
    
    def __init__(self, group = None, suit = None):
        self.group = group
        self.suit = suit
    
    def getCard(self):
        return f'Group: {self.group}, suit: {self.suit}'
    
    def update(self, newGroup, newSuit):
        self.group = newGroup
        self.suit = newSuit
        return self