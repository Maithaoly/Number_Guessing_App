from classRole import Role
from classCard import Card

class Player(Role):
    def __init__(self, card, point = 60):
        super().__init__(card)
        self.point = point
    
    def __str__(self):
        return f'YOUR CARD: {self.card.getCard}\nYOUR POINT: {self.point}'
    

    @property
    def getPoint(self):
        return self.point
    
    @getPoint.setter
    def getPoint(self, newPoint):
        self.point = newPoint
        return self
    
    def Guess(self):
        while True:
            res = None
            try:
                print('ENTER [1] TO CHOOSE GREATER OR ENTER [0] TO CHOOSE TO LESS THAN THE HOUSE')
                res = int(input('Player start guessing...'))
            except ValueError: 
                print('Oops! That was no valid number. Try again')
            if res in (0,1):
                break
            else:
                print('Oops! The number must be 0 or 1. Try again')
        return res

       
            
