from collections import namedtuple
import random
import re
from classCard import Card
from classHouse import House
from classPlayer import Player


# Create a list of 54 cards  
def listCard():
    suites = ('Spade', 'Club', 'Diamond', 'Heart')
    groups = list(range(3,10)) + ['J', 'Q', 'K', 'A']

    Card = namedtuple('Card', ['group', 'suit'])
    listCard = [Card(group, suit) for group in groups for suit in suites]
    listCard.append(Card('Jocker','Black'))
    listCard.append(Card('Jocker','Red'))
    return listCard


# Compare whether the player's card is greater or less than the house's
def Compare_Card(player_card, house_card):
    # If greater, return 1, otherwise return 0
    if listCard().index(player_card) > listCard().index(house_card):
        return 1
    else:
        return 0
    

# Compare whether the player predicted correctly with the result
def Compare_Result(player, player_card, house_card):
    # If true, return 1, otherwise return 0
    if Compare_Card(player_card, house_card) == player.Guess():
        return 1
    else:
        return 0
    

def checkInput(player, flag, flag2, count):
    # Receive input from the keyboard and check the condition
    while(True):
        temp = None
        try:
            temp = int(input('ENTER [1] TO CONTINUE OR ENTER [0] TO STOP...'))

        except ValueError:
            print('Oops! The number must be interger. Try again')
            
        if temp in (0,1):
            break
        else:
            print('Oops! The number must be 0 or 1. Try again')

    # If the input is 0, the reward will be added to the point,
        # the flag variable is on, so that if a player wants to play a new match, 25 points will be deducted,
        # the flag2 variable is on, to check the condition below
    # Otherwise the flag variable used is off.
    if temp == 0:
        flag = 1
        player.getPoint += count*10
        print('YOUR POINT: ',player.getPoint)
        flag2 =1
    else:
        flag = 0
    return flag, flag2, count


def checkInput2():

    # Receive input from the keyboard and check the condition
        # Use regex to search from input 
            # If the input is play or 1, return 1
            # If the input is exit or 0, return 0
    while(True):
        str = input('ENTER [1/play] TO PLAY AGAIN OR ENTER [0/exit] TO EXIT...')
        str = str.lower()
        pattern1 = '^(exit)|0'
        temp = re.fullmatch(pattern1, str)

        pattern2 = '^(play)|1'
        temp2 =re.fullmatch(pattern2, str)

        if temp:
            return 0
        elif temp2:
            return 1
        else:
            print('Oops! That was no valid number. Try again')



def initRole(List):
    # Choose a card of list card
    house_card = random.choice(List)
    # Create the house using this card
    house = House(Card(house_card.group, house_card.suit))
    # Remove this card from list card
    List.remove(house_card)

    # Choose a card of list card
    player_card = random.choice(List)
    # Create the house using this card
    player = Player(Card(player_card.group, player_card.suit))
    # Remove this card from list card
    List.remove(player_card)

    return List, house_card, house, player_card, player
    

def updateRole(List, house, player):
    # Choose a card of list cards
    house_card = random.choice(List)
    # Update the house using this card
    house.card.update(house_card.group, house_card.suit)
    # Remove this card from list card
    List.remove(house_card)

    # Choose a card of list card
    player_card = random.choice(List)
    # Update the house using this card
    player.card.update(player_card.group, player_card.suit)
    # Remove this card from list card
    List.remove(player_card)

    print('\nThe House receives and shows his card first:')
    print('-----------> ',house.getCard())

    return List, house,house_card, player, player_card


def winTheRound(player, flag, flag2, count):
    # If the player decides to continue,the count variable used to calculate the reward will be doubled on the next round
    count *= 2
    print('\n***************** YOU WIN THE ROUND *****************')
    print(player.getCard())
    print('YOUR REWARD:',count*10)
    print('YOUR POINT:',player.getPoint)

    # Receive input from the keyboard and check the condition
    flag, flag2, count = checkInput(player, flag, flag2, count)

    return player, flag, flag2, count


def loseTheRound(player):
    print('\n***************** YOU LOSE THE ROUND *****************')
    print(player.getCard())
    print('YOUR POINT:',player.getPoint)

    #  the count variable is on, the player's point will be recalculated from the beginning
    #  the flag2 variable is on, used to check the condition below
    count = 1
    flag2 = 1
    return count, flag2



def PlayGame():
    # Create a list cards of 54 cards
    List = listCard()

    # Using list cards to create house and player
    List, house_card, house, player_card, player = initRole(List)
    print('YOUR POINT:',player.getPoint )

    # Show the house's card first
    print('\nThe House receives and shows his card first:')
    print('-----------> ',house.getCard())

    # To start a match the player will be deducted 25 points 
    player.getPoint -= 25

    # The count variable used to calculate player's point
    count = 1

    # The flag variable used to mark a new match
    flag = 0

    while(True):
    
        flag2 = 0

        # If a new match occurs, the player will be deducted 25 points 
        # and the count variable will be recalculated from the beginning
        if flag == 1:
            count = 1
            player.getPoint -= 25
        print('YOUR POINT:',player.getPoint)

        # If the player guesses correctly 
        if Compare_Result(player, player_card, house_card):
            player, flag, flag2, count = winTheRound(player, flag, flag2, count)
        
            # Check if the player won the game or not 
            if player.getPoint >= 1000:
                print('---------------------- YOU WIN THE GAME ----------------------')
                print('YOUR POINT: ',player.getPoint)
                return 1
        # If the player guesses wrong, he will lose the reward 
        else:
            count, flag2 = loseTheRound(player)

        # If the flag2 variable is on
        # If the player has less than 30 points, he will lose the game
        # Otherwise ask the player if he wants to play again or quit
        if flag2 == 1:
            if player.point < 30:
                # if the player breaks the loop because it is less than 30 points, he loses the game
                print('\n---------------------- YOU LOSE THE GAME ----------------------')
                print('YOUR POINT: ',player.point)
                return 0
            else:
                temp = checkInput2()
                if temp == 0:
                    print('YOUR POINT: ',player.getPoint)
                    return 1
                else:
                    flag = 1
            
        # If the match countinues, update the cards for the house and the player
        List, house,house_card, player, player_card = updateRole(List, house, player)

 