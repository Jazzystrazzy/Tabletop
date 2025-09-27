from typing import Optional, Callable
from random import shuffle, choice
from cards.card import Card


class CardCollection:
    def __init__(self, cards: Optional[list[Card]] = None) -> None:
        # Always copy to avoid aliasing the caller's list
        self.cards: list[Card] = list(cards) if cards is not None else []

    # -------------------
    # Basic operations
    # -------------------
    def add_card(self, card: Card) -> None:
        """Add a card to the collection."""
        self.cards.append(card)

    def remove_card(self, card: Card) -> None:
        """Remove a specific card if present."""
        if card in self.cards:
            self.cards.remove(card)

    def to_list(self) -> list[Card]:
        """Return a shallow copy of all cards."""
        return list(self.cards)

    def shuffle(self) -> None:
        """Shuffle cards in place."""
        shuffle(self.cards)

    def clear_collection(self) -> None:
        """Remove all cards."""
        self.cards.clear()

    def count(self) -> int:
        """Number of cards in the collection."""
        return len(self.cards)

    def __contains__(self, card: Card) -> bool:
        return card in self.cards

    def __iter__(self):
        return iter(self.cards)

    def __len__(self) -> int:
        return len(self.cards)

    # -------------------
    # Searching
    # -------------------
    def find_card(self, condition: Callable[[Card], bool], nth: int = 1) -> Optional[Card]:
        """
        Find the nth card (1-based index) matching a condition.
        Returns None if not found.
        """
        matches = [c for c in self.cards if condition(c)]
        return matches[nth - 1] if len(matches) >= nth else None

    def find_all(self, condition: Callable[[Card], bool]) -> list[Card]:
        """
        Return a list of all cards matching the condition.
        """
        return [c for c in self.cards if condition(c)]

    # -------------------
    # Drawing
    # -------------------
    def draw_cards(
        self,
        n: int,
        condition: Optional[Callable[[Card], bool]] = None,
        from_where: str = "top",
    ) -> list[Card]:
        """
        Remove and return up to `n` cards matching an optional condition,
        drawn from 'top', 'bottom', or 'random'.
        """
        if from_where not in {"top", "bottom", "random"}:
            raise ValueError("Invalid from_where: must be 'top', 'bottom', or 'random'.")

        available = [c for c in self.cards if not condition or condition(c)]
        drawn: list[Card] = []

        for _ in range(min(n, len(available))):
            if from_where == "top":
                card = available[0]
            elif from_where == "bottom":
                card = available[-1]
            else:  # "random"
                card = choice(available)
            self.cards.remove(card)
            available.remove(card)
            drawn.append(card)

        return drawn

    # -------------------
    # Trading
    # -------------------
    def trade_card(self, other: "CardCollection", my_card: Card, their_card: Card) -> None:
        """Trade a specific card with another collection."""
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
        their_nth: int = 1,
    ) -> None:
        """
        Trade the nth card matching my_condition with the nth card matching their_condition.
        """
        my_card = self.find_card(my_condition, nth=my_nth)
        their_card = other.find_card(their_condition, nth=their_nth)

        if my_card and their_card:
            self.trade_card(other, my_card, their_card)


    def trade_all_by_condition(
        self,
        other: "CardCollection",
        my_condition: Callable[[Card], bool],
        their_condition: Callable[[Card], bool],
    ) -> None:
        """
        Trade all cards that match the given conditions.
        """
        my_matches = [c for c in self.cards if my_condition(c)]
        their_matches = [c for c in other.cards if their_condition(c)]
        for my_card, their_card in zip(my_matches, their_matches):
            self.trade_card(other, my_card, their_card)


    # -------------------
    # Read-only view
    # -------------------
    @property
    def cards_view(self) -> tuple[Card, ...]:
        """
        Return an immutable tuple of all cards
        for safe read-only access.
        """
        return tuple(self.cards)
