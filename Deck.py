#deck 52 cards
#shuffle
#deal
import Card
class Deck(Card):

    def __init__(self):
        self.all_cards = []
        for suit in Card.suit:
            for rank in Card.rank:
                #creat card deck
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)



new_deck2 = Deck()
print(new_deck2.all_cards[0])
