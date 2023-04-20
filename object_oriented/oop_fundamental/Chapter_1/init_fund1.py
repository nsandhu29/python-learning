class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.hard, self.soft = self._points()
    
class NumberCard( Card ):
    def _points(self):
        return (int(self.rank), int(self.rank))

class AceCard(Card):
    def _points(self):
        return 1, 11

class FaceCard(Card):
    def _points(self):
        return 10, 10

class Suit:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

