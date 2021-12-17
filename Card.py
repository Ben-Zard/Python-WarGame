#cards
#suit,rank,value,
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
class Card():

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]


    def __str__(self):
        return (f"{self.rank} of {self.suit}")


class Deck():

    def __init__(self):
        # Note this only happens once upon creation of a new Deck
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                # This assumes the Card class has already been defined!
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Player():
    #hold current list
    #add single or multiple cards
    #hold top and boottom of card(draw from top) pick up to bottom
    def __init__(self,name):
        #draw card
        self.name = name
        self.all_cards = []

    def remove_one(self):
        #removes one card
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            #multiple cards
            self.all_cards.extend(new_cards)
        else:
            #single card
            self.all_cards.append(new_cards)

    def __str__(self):
        return(f"Player {self.name} has {len(self.all_cards)} cards")
        #add card


#create two players

#create deck and split it evenly

#play game- check for card = 0 and if not then game is one

#while game on then remove one card and compare
    # if tie then draw again (while at war)
    #if win then add to bottom of deck
game_on = True
round_number = 0
player_one = Player("One")
player_two = Player("Two")
new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

while game_on:
  round_number +=1
  print(f"It is currently round {round_number}")
  if len(player_one.all_cards) == 0:
      print(f"{player_one} left\n Player 2 wins!")
      game_on = False

  if len(player_two.all_cards) == 0:
      print(f"{player_two} left\n Player 1 wins!")
      game_on = False

  player_one_cards = []
  player_one_cards.append(player_one.remove_one())

  player_two_cards = []
  player_two_cards.append(player_two.remove_one())

  at_war = True
  while at_war:

      if player_one_cards[-1].value > player_two_cards[-1].value:
          # Player One gets the cards
          player_one.add_cards(player_one_cards)
          player_one.add_cards(player_two_cards)
          at_war = False

      elif player_two_cards[-1].value > player_one_cards[-1].value:
          player_two.add_cards(player_one_cards)
          player_two.add_cards(player_two_cards)
          at_war = False

      else:
          print("WAR TIME!")
          if  len(player_one.all_cards) < 5:
              print("WAR TIME! can not happen Player 1 has less than 5 cards\nPlayer 2 WINS")
              #can break this into an else to say who explisistly won
              at_war = False
              game_on = False

          elif len(player_two.all_cards) < 5:
              print("WAR TIME! can not happen Player 2 has less than 5 cards\nPlayer 1 WINS")
              at_war = False
              game_on = False

          else:
              for num in range(5):
                  player_one_cards.append(player_one.remove_one())
                  player_two_cards.append(player_two.remove_one())





# new_deck2 = Deck()
# print(new_deck2)
# print(len(new_deck2.all_cards))
# print(new_deck2.all_cards[0])
# new_deck2.shuffle()
# print(new_deck2.all_cards[0])
# mycard = new_deck2.deal_one()
# print(mycard)
# print(len(new_deck2.all_cards))
# new_player = Player("Ben")
# print(new_player)
# new_player.add_cards([mycard])
# print(new_player)
# print(new_player.all_cards[0])
