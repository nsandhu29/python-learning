from init_fund1 import *
from functools import partial
# Define function that create objects of the required class
def card(rank, suit):
    """Function to create objects of Card class"""
    if rank == 1:
        return AceCard('A', suit)
    elif 2 <= rank < 11:
        return NumberCard(str(rank), suit)
    elif 11 <= rank < 14:
        name = {11: 'J', 12: 'Q', 13: 'K'}[rank]
        return FaceCard(name, suit)
    else:
        raise Exception("Rank out of range")

deck = [card(rank, suit)
        for rank in range(1, 14)
            for suit in ('Club','Diamond', 'Heart', 'Spade')]


def card1(rank, suit):
    """Function to create onject of card class using mapping"""
    assert(1 <= rank < 14), "Rank out of range"
    class_ = {1: AceCard, 11: FaceCard, 12: FaceCard,
              13: FaceCard}.get(rank, NumberCard)
    return class_(rank, suit)

def card2(rank, suit):
    """Function to create mapping with string rank"""
    assert(1 <= rank < 14), "Rank out of range"
    class_ = {1: AceCard, 11: FaceCard, 12: FaceCard,
              13: FaceCard}.get(rank, NumberCard)
    rank_str = {1:'A', 11:'J', 12:'Q', 13:'K'}.get(rank, str(rank))
    return class_(rank_str, suit)

# Above function involves repetition

def card3(rank, suit):
    """Function to create mapping using tuple of values"""
    assert(1 <= rank < 14), "Rank out of range"
    class_, rank_str = {1: (AceCard, 'A'),
             11: (FaceCard, 'J'),
             12: (FaceCard, 'Q'),
             13: (FaceCard, 'K')}.get(rank, (NumberCard, str(rank)))
    return class_(rank_str, suit)


def card4(rank, suit):
    """Function to create mapping using partial"""
    assert(1 <= rank < 14), "Rank out of range"
    part_class = {
        1: partial(AceCard, 'A'),
        11: partial(FaceCard, 'J'),
        12: partial(FaceCard, 'Q'),
        13:partial(FaceCard, 'K')
    }.get(rank, partial(NumberCard, str(rank)))
    return part_class(suit)