from random import choice
from typing import Callable, Optional
from cards.collection import CardCollection
from cards.card import Card

class Deck(CardCollection):
    def __init__(self, cards: Optional[list[Card]] = None):
        super().__init__(cards)

    def draw_n_cards(self, *args, **kwargs):
        return super().draw_cards(*args, **kwargs)


class FrenchDeck(Deck):
    def __init__(self):
        ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        suits = ['♦️','❤️','♠️','♣️']
        values = {
            'A':14,
            'K':13,
            'Q':12,
            'J':11,
            '10':10,
            '9':9,
            '8':8,
            '7':7,
            '6':6,
            '5':5,
            '4':4,
            '3':3,
            '2':2
            }
        
        cards = [Card(f"{rank}{suit}", attributes={"color": 'red' if suit in ('♦️','❤️') else 'black', "value": values[rank]}) for rank in ranks for suit in suits]
        super().__init__(cards)    