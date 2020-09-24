class Card:
    def __init__(self):
        self.card = []

    def create_cards(self):
        suit = ["circle", "triangle", "cross", "box", "star", "whot!"]
        val = range(1, 15)
        for num in val:
            if num == 6 or num == 9:
                continue
            circle = suit[0] + " " + str(num)
            self.card.append(str(circle))

        for num in range(1, 15):
            if num == 6 or num == 9:
                continue
            triangle = suit[1] + " " + str(num)
            self.card.append(str(triangle))

        for num in range(1, 15):
            if num == 4 or num == 6 or num == 8 or num == 9 or num == 12:
                continue
            cross = suit[2] + " " + str(num)
            self.card.append(str(cross))

        for num in range(1, 15):
            if num == 4 or num == 6 or num == 8 or num == 9 or num == 12:
                continue
            box = suit[3] + " " + str(num)
            self.card.append(str(box))

        for num in range(1, 15):
            if num == 6 or num == 9 or num == 10 or num == 11 or num == 12 or num == 13 or num == 14:
                continue
            star = suit[4] + " " + str(num)
            self.card.append(str(star))
        return self.card
        # print(self.card)

    def show(self):
        print(self.card)

    def shuffle(self):
        import random
        random.shuffle(self.card)

class Hand(object):
    def __init__(self):
        self.card = []

    def clear(self):
        self.card = []

    def add(self, card):
        self.cards.append(card)
        
class Deck(Hand):
    def market(self, card):
        self.card.pop()

    def build(self):
        pass

    def drawCard(self):
        return self.card.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def draw(self, deck):
        self.hand.append(deck.drawCard())

    def showHand(self):
        for card in self.hand:
            card.show()
        

stack = Card()
stack.create_cards()
stack.shuffle()
stack.show()