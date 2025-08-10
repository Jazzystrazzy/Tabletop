from typing import Optional
from cards.collection import CardCollection
from cards.card import Card

class Deck(CardCollection):
    def __init__(self, cards: Optional[list[Card]] = None):
        super().__init__(cards)
    