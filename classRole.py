from classCard import Card

class Role():

    def __init__(self, card: Card):
        self.card = card
    def getCard(self):
        return self.card.getCard()