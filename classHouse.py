from classRole import Role
from classCard import Card

class House(Role):
    def __init__(self, card):
        super().__init__(card)

    def __str__(self):
        return f'HIS CARD: {self.card.getCard}'