from typing import Optional, Callable
from random import shuffle
from cards.card import Card

class CardCollection:
    def __init__(self, cards: Optional[list[Card]] = None):
        self.cards = cards if cards else []

    # -------------------
    # Basic operations
    # -------------------
    def add_card(self, card: Card):
        self.cards.append(card)

    def remove_card(self, card: Card):
        if card in self.cards:
            self.cards.remove(card)

    def get_cards(self):
        return self.cards.copy()
    
    def shuffle(self):
        shuffle(self.cards)

    def clear_collection(self):
        self.cards.clear()

    def count(self):
        return len(self.cards)

    def __contains__(self, card):
        return card in self.cards

    def __iter__(self):
        return iter(self.cards)

    def __len__(self):
        return len(self.cards)

    # -------------------
    # Searching
    # -------------------
    def find_card(self, condition: Callable[[Card], bool], nth: int = 1) -> Optional[Card]:
        """
        Find the nth card matching a condition (1-based index).
        Returns None if not found.
        """
        matches = [c for c in self.cards if condition(c)]
        return matches[nth - 1] if len(matches) >= nth else None

    def find_all(self, condition: Callable[[Card], bool]) -> list[Card]:
        """
        Return all cards matching the condition.
        """
        return [c for c in self.cards if condition(c)]

    # -------------------
    # Trading
    # -------------------
    def trade_card(self, other: "CardCollection", my_card: Card, their_card: Card):
        self.remove_card(my_card)
        other.remove_card(their_card)
        self.add_card(their_card)
        other.add_card(my_card)

    def trade_by_condition(
        self,
        other: "CardCollection",
        my_condition: Callable[[Card], bool],
        their_condition: Callable[[Card], bool],
        my_nth: int = 1,
        their_nth: int = 1
    ):
        """
        Trade the nth card matching my_condition with the nth card matching their_condition.
        """
        my_card = self.find_card(my_condition, nth=my_nth)
        their_card = other.find_card(their_condition, nth=their_nth)

        if my_card and their_card:
            self.trade_card(other, my_card, their_card)
