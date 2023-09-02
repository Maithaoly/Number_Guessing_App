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

        
class Role():

    def __init__(self, card: Card):
        self.card = card
    def getCard(self):
        return self.card.getCard()


class House(Role):
    def __init__(self, card):
        super().__init__(card)

    def __str__(self):
        return f'HIS CARD: {self.card.getCard}'
    
    

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
            try:
                print('ENTER [1] TO CHOOSE GREATER OR ENTER [0] TO CHOOSE TO LESS THAN THE HOUSE')
                res = int(input('Player start guessing...'))
                break
            except ValueError: 
                print('Oops! That was no valid number. Try again')
        return res
    
  


from collections import namedtuple
import random
import re

def listCard():
    suites = ('Spade', 'Club', 'Diamond', 'Heart')
    groups = list(range(3,10)) + ['J', 'Q', 'K', 'A']

    Card = namedtuple('Card', ['group', 'suit'])
    listCard = [Card(group, suit) for group in groups for suit in suites]
    listCard.append(Card('Jocker','Black'))
    listCard.append(Card('Jocker','Red'))
    return listCard


def Compare_Card(player_card, house_card):
    if listCard().index(player_card) > listCard().index(house_card):
        return 1
    else:
        return 0
    
def Compare_Result(player, player_card, house_card):
    if Compare_Card(player_card, house_card) == player.Guess():
        return 1
    else:
        return 0

def PlayGame():
    List = listCard()

    house_card = random.choice(List)
    house = House(Card(house_card.group, house_card.suit))
    List.remove(house_card)

    player_card = random.choice(List)
    player = Player(Card(player_card.group, player_card.suit))
    List.remove(player_card)
    
    print('\nThe House receives and shows his card first:')
    print('-----------> ',house.getCard())
    player.getPoint -= 25

    count = 1
    flag = 0

    

    while(True):
        flag2 = 0
        if flag == 1:
            player.getPoint -= 25
        print('YOUR POINT:',player.getPoint)
        
        if Compare_Result(player, player_card, house_card):
            count *= 2
            print('\n***************** YOU WIN THE ROUND *****************')
            print(player.getCard())
            #player.getPoint += count*10
            print('YOUR REWARD:',count*10)
            print('YOUR POINT:',player.getPoint )


            if player.getPoint >= 1000:
                print('---------------------- YOU WIN THE GAME ----------------------')
                print('YOUR POINT: ',player.getPoint + count*10)
                return 1
        
            while(True):
                try:
                    temp = int(input('ENTER [1] TO CONTINUE OR ENTER [0] TO STOP...'))
                    break
                except ValueError:
                    print('Oops! That was no valid number. Try again')

            if temp == 0:
                flag = 1
                player.getPoint += count*10
                print('YOUR POINT: ',player.getPoint)
                flag2 =1
            else:
                flag = 0
        else:
            print('\n***************** YOU LOSE THE ROUND *****************')
            print(player.getCard())
            print('YOUR POINT:',player.getPoint)
            count = 1
            flag2 = 1
        if flag2 == 1:
            if player.point < 30:
                break
            else:
                str = input('ENTER [1/play] TO PLAY AGAIN OR ENTER [0/exit] TO EXIT...')
                str.lower()
                pattern = '^(exit)|0'
                temp = re.match(pattern, str)
                if temp:
                    temp = 0
                else:
                    temp = 1
                if temp == 0:
                    print('YOUR POINT: ',player.getPoint)
                    return 1
                else:
                    flag = 1
    
        del house_card
        house_card = random.choice(List)
        house.card.update(house_card.group, house_card.suit)
        List.remove(house_card)
        

        del player_card
        player_card = random.choice(List)
        player.card.update(player_card.group, player_card.suit)
        List.remove(player_card)
        
        print('\nThe House receives and shows his card first:')
        print('-----------> ',house.getCard())
    print('\n---------------------- YOU LOSE THE GAME ----------------------')
    print('YOUR POINT: ',player.point)
    return 0
 
